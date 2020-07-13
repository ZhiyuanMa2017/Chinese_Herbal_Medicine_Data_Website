from rdkit import Chem
from rdkit.Chem import rdFMCS
inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf2=open(r'C:\Users\admin\PycharmProjects\temp\Data2.sdf')
# w=Chem.SDWriter('Data8.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl2=Chem.ForwardSDMolSupplier(inf2)
for mol in fsuppl1:
    w.write(mol)
for mol2 in fsuppl2:
    w.write(mol2)
w.close()

ww=Chem.SDWriter('Data12.sdf')
for mol in fsuppl1:
    ww.write(mol)
for mol2 in fsuppl2:
    n=1
    if mol is None: continue
    for mol in fsuppl1:
        if mol2 is None: continue
        res = rdFMCS.FindMCS([mol,mol2])
        if res.numAtoms == mol.GetNumAtoms() and res.numAtoms == mol2.GetNumAtoms():
            n=2
    if n==1:
        ww.write(mol2)
ww.close()

inf10=open(r'C:\Users\admin\PycharmProjects\temp\Data12.sdf')
fsuppl10=Chem.ForwardSDMolSupplier(inf10)
m=0
numlist=[]
for mol in fsuppl10:
    if mol is None:continue
    numlist.append(mol.GetNumAtoms())
print(len(numlist))

inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf2=open(r'C:\Users\admin\PycharmProjects\temp\Data2.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl2=Chem.ForwardSDMolSupplier(inf2)
for mol2 in fsuppl2:
    for mol in fsuppl1:
        if mol.HasSubstructMatch(mol2) and mol2.HasSubstructMatch(mol):
            print(Chem.MolToSmiles(mol2))

from rdkit import Chem
from rdkit.Chem import rdFMCS
w=Chem.SDWriter('Data1copy.sdf')
inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf2=open(r'C:\Users\admin\PycharmProjects\temp\Data2.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl2=Chem.ForwardSDMolSupplier(inf2)
for mol in fsuppl1:
    w.write(mol)
w.close()

inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf1copy=open(r'C:\Users\admin\PycharmProjects\temp\Data1copy.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl1copy=Chem.ForwardSDMolSupplier(inf1copy)
list1=[]
list2=[]
for mol2 in fsuppl1:
    list1.append(mol2)
for mol in fsuppl1copy:
    list2.append(mol)
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i].HasSubstructMatch(list2[j]) and list2[j].HasSubstructMatch(list1[i]):
            print Chem.MolToSmiles(list1[i])

inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf2=open(r'C:\Users\admin\PycharmProjects\temp\Data2.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl2=Chem.ForwardSDMolSupplier(inf2)
list1=[]
list2=[]
for mol2 in fsuppl1:
    list1.append(mol2)
for mol in fsuppl2:
    list2.append(mol)
for i in range(len(list1)):
    n=1
    for j in range(len(list2)):
        if list1[i].HasSubstructMatch(list2[j]) and list2[j].HasSubstructMatch(list1[i]):
            n=0
    if n==1:
        list2.append(list1[i])


www=Chem.SDWriter('Data1&2.sdf')
for i in list2:
    www.write(i)
www.close()


inf111=open(r'C:\Users\admin\PycharmProjects\temp\Data1&2.sdf')
fsuppl111=Chem.ForwardSDMolSupplier(inf111)
list111=[x for x in fsuppl111]



