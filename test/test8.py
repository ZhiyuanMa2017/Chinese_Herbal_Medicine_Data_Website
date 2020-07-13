import xlrd
fname = 'C:\Users\Administrator\PycharmProjects\zhongyao\herb.xlsx'
workbook = xlrd.open_workbook(fname)
booksheet = workbook.sheet_by_name('Sheet1')
p = list()
for row in range(booksheet.nrows):
    row_data = []
    for col in range(booksheet.ncols):
        cel = booksheet.cell(row, col)
        val = cel.value
        row_data.append(val)
    p.append(row_data)
#
# import rdkit
#
# from rdkit import Chem
# m=Chem.MolFromMol2File('C:\Users\Administrator\PycharmProjects\zhongyao\st\MOL000010.mol2')
# mm=Chem.MolToSmiles(m)
# print  mm
import MySQLdb
db = MySQLdb.connect("localhost","root","wangsishabi","tcm" )
cur = db.cursor()
db.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')

for i in range(len(p)):
    wangzhi = 'http://hulab.rxnfinder.org/smi2img/%s/' % p[i][8]
    cur.execute("INSERT INTO shop_product(slug,name,herbname,image,description,xiangsidu,cass,pubchem,inchikey,druglikeness,category_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"% (i+1,p[i][1],p[i][6],wangzhi,p[i][8],1,p[i][5],p[i][4],p[i][3],p[i][2],p[i][7]))
    wangzhi = ''
cur.close()
db.commit()
db.close()