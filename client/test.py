__author__ = 'mohamed'
import Client.Client as Client
def test_clone():
    c=Client("git")
    return c.Clone("git@github.com:mkalioby/CD_Project.git","/tmp/CD_Project/","""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAs53ey/L9eX7WKi7UtlJo+1Rw9DmWj5XLIWfn9FOyUNFeUOS9
DcgTe7dFMfpiTMBXQ2mzdgN7NtlxPZts7cIF3YXkftPHz5Afhezi6PXgfJOZcfkN
srLzvfxChG2q7+v4Ktar+jbj/Y59JYvPJTBBUWlPDhqVgLMhaA3kFtIeg+7AesUW
M1Ituuk+zWl+hzQyZk4tyZ9fKrJqhu1UxQnYi1CTWlXx42E8Xzk9iV3UGfimdYl+
jTgD7S+bvoFgQYysRp7AubiW2DTMcUt8Yh/Za89WFhHqy8R/nMW6ek+0O1Ze1LAd
orbg3hasBrQgTgP1Vp/LnDVjFKJ/0KLkgJCaRwIDAQABAoIBAQCZodcHq3eTjCGz
Qws+R470Km3S988IUZ/FmxKTsWM8LVj26C+ssg24LDJLZVbfP0Vkq+yMbL3fVG2/
vEmXs/VAXV3r/UlTCHtuGgicKnMxGy6MhfJpfxds0XAzxXoIbVV/js7a3kh0gIQa
sVMlA/laoTC1Z5eo1Y8laXxG6MKhJQ7U/KS9KK3SWT+XZxEkaiV03TyvgdWWYsbA
QiUKUa+oCPKxgVUDVERsnrDL9e47Pma6ct7VJWc12rXUDhGhoF0CloGI4QoSfOGG
7lOENljsBhsQjr41Mm0iVob8KRDJ+dkvdl8a/BMJB4tFIhsrMp3gqSRNyRRlFpJq
ZeR4bvxBAoGBAOCUJpo02QVDys+wPAOw52GxfpW0HBqLDPua6NVaf8L+vLjBtFte
Cp4XDtjgoFm3tNnr/NLhegf9jrERa0spgPK7jTQ3edNTJbyiyR8QWgeqRuravIzr
ZClq0FMHTNGamW1e2hstL2nhCIqJID4wdt8J2dXX+uIOFZ5xsmYXD/mzAoGBAMy/
SqpZPNykPmSpek9q8g3VbJ0tYHas6B9fIoqvYH+aIRXYOFZ0MpiUEiVVAgtGn5DM
gros1kvlY9metdLSLpXVzYnhjY5YawBx0iVDZ/ARsePgR76tCrmMXaHR2wolDi6v
0aHIFWAYJv3PpaNJqKqByjZBaLXvvS6HMxDHTusdAoGBAIlt/+V0G65eGvlXhpJX
qnCdNrKT4nLXzt0VohAV7oM8ce66Ew2qkeLGh35uj5H3moOVJ0VBV/UV1EFFQJxh
TJi97x4aKMIKathx4ZPR5NY1/Gnx61ptHgE+bTeyCu9lpShJ2DyzPQWVAS4N1h5Y
eBXrKFP1dIDrT42DVEGnMU6DAoGBAL3gVLT/xvJzmq0tgpEuA8YSfASTdVb5aNbX
Gih1Fc+gNziT6UM7xUQ8ZUubtyaP2yCkmENhm2aNF/lUNxiI9MzdlxxcQTOWCb1C
0Pjftv8q2ccTUlWhEkYaxyZvgGu7C5j+UjFvZWtVWqucquZwQ+vEK6v/IsU+zDnf
Bdt0ilp9AoGAbQ0JvhO7UozrP+x6cYjccOm76pDGnuPzByIlm6Hmckce6wjOJKUv
/S2BW1etxhhSt33YcDl5EGeLNUeITSTs0B6CkmhEAopnQfBotBAJBlu/uWF6mQSp
u7Kcu+PqQ1vWMOTM6GpWEAd6Xol2WvP6WolIH4udOR05i/l7dhXRM6Q=
-----END RSA PRIVATE KEY-----""")

def test_pull():
    c=Client("git")
    return c.Pull("git@github.com:mkalioby/CD_Project.git","/tmp/CD_Project/","""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAs53ey/L9eX7WKi7UtlJo+1Rw9DmWj5XLIWfn9FOyUNFeUOS9
DcgTe7dFMfpiTMBXQ2mzdgN7NtlxPZts7cIF3YXkftPHz5Afhezi6PXgfJOZcfkN
srLzvfxChG2q7+v4Ktar+jbj/Y59JYvPJTBBUWlPDhqVgLMhaA3kFtIeg+7AesUW
M1Ituuk+zWl+hzQyZk4tyZ9fKrJqhu1UxQnYi1CTWlXx42E8Xzk9iV3UGfimdYl+
jTgD7S+bvoFgQYysRp7AubiW2DTMcUt8Yh/Za89WFhHqy8R/nMW6ek+0O1Ze1LAd
orbg3hasBrQgTgP1Vp/LnDVjFKJ/0KLkgJCaRwIDAQABAoIBAQCZodcHq3eTjCGz
Qws+R470Km3S988IUZ/FmxKTsWM8LVj26C+ssg24LDJLZVbfP0Vkq+yMbL3fVG2/
vEmXs/VAXV3r/UlTCHtuGgicKnMxGy6MhfJpfxds0XAzxXoIbVV/js7a3kh0gIQa
sVMlA/laoTC1Z5eo1Y8laXxG6MKhJQ7U/KS9KK3SWT+XZxEkaiV03TyvgdWWYsbA
QiUKUa+oCPKxgVUDVERsnrDL9e47Pma6ct7VJWc12rXUDhGhoF0CloGI4QoSfOGG
7lOENljsBhsQjr41Mm0iVob8KRDJ+dkvdl8a/BMJB4tFIhsrMp3gqSRNyRRlFpJq
ZeR4bvxBAoGBAOCUJpo02QVDys+wPAOw52GxfpW0HBqLDPua6NVaf8L+vLjBtFte
Cp4XDtjgoFm3tNnr/NLhegf9jrERa0spgPK7jTQ3edNTJbyiyR8QWgeqRuravIzr
ZClq0FMHTNGamW1e2hstL2nhCIqJID4wdt8J2dXX+uIOFZ5xsmYXD/mzAoGBAMy/
SqpZPNykPmSpek9q8g3VbJ0tYHas6B9fIoqvYH+aIRXYOFZ0MpiUEiVVAgtGn5DM
gros1kvlY9metdLSLpXVzYnhjY5YawBx0iVDZ/ARsePgR76tCrmMXaHR2wolDi6v
0aHIFWAYJv3PpaNJqKqByjZBaLXvvS6HMxDHTusdAoGBAIlt/+V0G65eGvlXhpJX
qnCdNrKT4nLXzt0VohAV7oM8ce66Ew2qkeLGh35uj5H3moOVJ0VBV/UV1EFFQJxh
TJi97x4aKMIKathx4ZPR5NY1/Gnx61ptHgE+bTeyCu9lpShJ2DyzPQWVAS4N1h5Y
eBXrKFP1dIDrT42DVEGnMU6DAoGBAL3gVLT/xvJzmq0tgpEuA8YSfASTdVb5aNbX
Gih1Fc+gNziT6UM7xUQ8ZUubtyaP2yCkmENhm2aNF/lUNxiI9MzdlxxcQTOWCb1C
0Pjftv8q2ccTUlWhEkYaxyZvgGu7C5j+UjFvZWtVWqucquZwQ+vEK6v/IsU+zDnf
Bdt0ilp9AoGAbQ0JvhO7UozrP+x6cYjccOm76pDGnuPzByIlm6Hmckce6wjOJKUv
/S2BW1etxhhSt33YcDl5EGeLNUeITSTs0B6CkmhEAopnQfBotBAJBlu/uWF6mQSp
u7Kcu+PqQ1vWMOTM6GpWEAd6Xol2WvP6WolIH4udOR05i/l7dhXRM6Q=
-----END RSA PRIVATE KEY-----""")

def testTagsList():
    c=Client("git")
    return c.ListTags("/tmp/SGP_Registry")
if __name__=="__main__":
    #print test_clone()
    #print test_pull()
    print testTagsList()
