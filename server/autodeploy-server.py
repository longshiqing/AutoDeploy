#!/usr/bin/python
from Crypto.PublicKey import RSA
import socket
import threading
import base64
import config
import Response
import Request
import Common
import scm.Git as git
from deployer import autodeployer
import  traceback
import yaml
JOBS = {}
EOM = Common.EOM
debug = False

def startServer():
    port = int(config.port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(5)
    print "Server started at " + str(port)
    return s


def importKey():
    file = open(config.publicKey, 'r')
    st = "".join(file.readlines())
    key = RSA.importKey(st)
    return key


def validReq(req):
    key = importKey()
    decrypted = key.decrypt(base64.decodestring(req["sec"]))
    if (req["Owner"]+req["scm"]+req["requestType"] == decrypted):
        return True
    else:
        return False


def HandleClient(clientsock):
    name = threading.currentThread().getName()
    print name, ' Started.............'
    global EOM
    chunks = []
    cmd=""
    while 1:
        buf = clientsock.recv(2048)
        if len(buf)<6:
            chunks[-1]+=buf
        else:
            chunks.append(str(buf))
        if (EOM in chunks[-1]):
            msg = "".join(chunks)[:-5]
            if debug: print msg
            if (msg == "TEST: HELLO"):
                Response.sendData(clientsock,"Hello")
                clientsock.close()
                return
            req = Request.parseRequest(msg)
            if (not validReq(req)):
                Response.sendData(clientsock, "Invalid Request")
                print "invalid request"
                clientsock.close()
                return
            if (req["requestType"]=="CLONE"):
                job = Request.parseCloneJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(job["workdir"],job["repo"])
                    gclient.setKey(job["key"])
                    cmd=gclient.get_clone_cmd()
            elif (req["requestType"] == "PULL"):
                job = Request.parsePullJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    gclient.setKey(job["key"])
                    cmd=gclient.get_pull_cmd()
            elif req["requestType"]=="LIST-TAGS":
                job = Request.parseListTagsJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    gclient.setKey(job["key"])
                    cmd=gclient.get_list_tags_cmd()
                    result=[]
                    res=Common.run(cmd)
                    if "ERR:" in res:
                        Response.sendData(clientsock,res)
                    else:
                        for line in res.split("\n"):
                            try:
                                cmd="cd %s; git show %s"%(job["workdir"],line)
                                res=Common.run(cmd)
                                lines=res.split("diff --git ")[0]
                                info=lines.split("\n")
                                #print info
                                tag=info[0][4:]
                                tagger=info[1].split(": ")[1].split("<")[0].strip()
                                date=info[2].split(": ")[1].strip()
                                commit=info[6].split("commit ")[1]
                                result.append(",,".join([tag,tagger,date,commit]))
                            except:
                                pass
                        Response.sendData(clientsock,"\n".join(result))
                        return
            elif req["requestType"] == "LIST-BRNACHS":
                job = Request.parseListBranchsJob(msg)
                if job["scm"] == "git":
                    gclient = git.GIT(workdir=job["workdir"])
                    cmd = gclient.get_list_branches()
                    result = []
                    res = Common.run(cmd)
                    print res
                    if "ERR:" in res:
                        Response.sendData(clientsock, res)
                    else:
                        for line in res.split("\n"):
                            try:
                                if line!="":
                                    result.append(line.replace("*","").strip())
                            except:
                                pass
                        print result
                        Response.sendData(clientsock, "\n".join(result))
                        return
            elif req["requestType"]=="LIST-COMMITS":
                job = Request.parseGetCommitsJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    gclient.setKey(job["key"])
                    cmd=gclient.get_history_cmd(job["options"])
            elif req["requestType"]=="SWITCH-TAG":
                job = Request.parseSwitchTagJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    cmd=gclient.get_switch_to_tag_cmd(tag=job["tag"])
            elif req["requestType"]=="SWITCH-COMMIT":
                job = Request.parseSwitchCommitJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    cmd=gclient.switch_to_histroy_cmd(commit=job["commit"])
            elif req["requestType"]=="DIFF-COMMIT":
                job = Request.parseSwitchCommitJob(msg)
                if job["scm"]=="git":
                    gclient=git.GIT(workdir=job["workdir"])
                    cmd=gclient.commit_diff_cmd(commit=job["commit"])

            elif req["requestType"]=="LIST-CHANGES":
                job = Request.parseGetChangeLog(msg)
                if job["scm"] == "git":
                    gclient = git.GIT(workdir=job["workdir"])
                    cmd = gclient.get_changelog(since=job["options"]["since"], to=job["options"]["to"])
                    result = []
                    res = Common.run(cmd)
                    print res
                    if "ERR:" in res:
                        Response.sendData(clientsock, res)
                    else:
                        for line in res.split("\n"):
                            try:
                                if line != "":
                                    result.append(line.replace("*", "").strip())
                            except:
                                pass
                        print result
                        Response.sendData(clientsock, "\n".join(result))
            elif req["requestType"]=="DEPLOY":
                print msg
                job = Request.parseDeployJob(msg)
                try:
                    config=yaml.safe_load(open(job["configFile"]))
                    autodeployer.deploy(config,job["workdir"])
                    res="Done"
                except Exception as e:
                    res="ERR:"+traceback.format_exc()
            if cmd!="":
                print cmd
                res=Common.run(cmd)
		print res
            Response.sendData(clientsock,res)
            if debug:
                print "Ended,",res
            else:
                print "Ended"
            clientsock.close()

            break
import os
if not os.geteuid()==0:
    print "The user should be a root."
    exit(-6)
f=open('/var/run/autodeploy-server', "w")
f.write(str(os.getpid()))
f.close()
import  sys
if "--debug" in sys.argv:  debug=True
s = startServer()
i = 0
while 1:
    clientsock, clientaddr = s.accept()
    i += 1
    print 'Got connection from ', clientsock.getpeername()
    t = threading.Thread(target=HandleClient, args=[clientsock], name="Thread #" + str(i))
    t.start()

exit(0)
