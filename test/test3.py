import sys

blocks = []
for ln in aaa.splitlines():
    if ln.startswith('/'):
        blocks.append()
    elif not ln.strip():
        continue
reload(sys)
sys.setdefaultencoding('utf-8')
templist=aaa.splitlines()
strlist=[]
for i in range(len(templist)):
    if templist[i].startswith('>'):
        strlist.append(templist[i+1])
for s in strlist:
    print s.decode('gb18030').encode('utf-8')
