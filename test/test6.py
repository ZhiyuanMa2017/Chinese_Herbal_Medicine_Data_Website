import MySQLdb
import rdkit
from rdkit import Chem
db = MySQLdb.connect("localhost","root","wangsishabi","tcm" )
cur = db.cursor()
db.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
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
    wangzhi = 'http://hulab.rxnfinder.org/smi2img/%s/' % structurelist[i].strip()
    cur.execute("INSERT INTO shop_product(slug,name,description,category_id,image) VALUES ('%s','%s','%s','%s','%s')" % (i+1,strlist[i].decode('gb2312'),structurelist[i],'1',wangzhi))
    wangzhi = ''
cur.close()
db.commit()
db.close()
