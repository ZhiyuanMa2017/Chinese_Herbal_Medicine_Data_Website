import MySQLdb
import rdkit
from rdkit import Chem
db = MySQLdb.connect("localhost","root","wangsishabi","tcm1" )
cur = db.cursor()
cur.execute("create table tcm1(name varchar(1000),struct varchar(1000))")
#读文件
data1=open('Data1&2.sdf').read()
templist=data1.splitlines()
strlist=[]
for i in range(len(templist)):
    if templist[i].startswith('>'):
        strlist.append(templist[i+1])
inf=open('Data1&2.sdf')
fsuppl=Chem.ForwardSDMolSupplier(inf)
structurelist=[]
for mol in fsuppl:
    structurelist.append(Chem.MolToSmiles(mol))
for i in range(len(strlist)):
    cur.execute("INSERT INTO tcm1(name,struct) VALUES ('%s','%s')" % (strlist[i],structurelist[i]))
cur.close()
db.commit()
db.close()


