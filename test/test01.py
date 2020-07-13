


from rdkit import Chem
from rdkit.Chem import rdFMCS
inf1=open(r'C:\Users\admin\PycharmProjects\temp\Data1.sdf')
inf2=open(r'C:\Users\admin\PycharmProjects\temp\Data2.sdf')
w=Chem.SDWriter('Data7.sdf')
fsuppl1=Chem.ForwardSDMolSupplier(inf1)
fsuppl2=Chem.ForwardSDMolSupplier(inf2)
for mol in fsuppl1:
    w.write(mol)
for mol2 in fsuppl2:
    n=1
    for mol in fsuppl1:
        res = rdFMCS.FindMCS([mol, mol2])
        if res.numAtoms == mol.GetNumAtoms() and res.numAtoms == mol2.GetNumAtoms():
            n=0
    if n==1:
        w.write(mol2)
    print(mol.GetNumAtoms())
    print (Chem.MolToSmiles(mol))
m1=Chem.MolFromSmiles('C1CSSSC1')
for mol in fsuppl2:
    if mol is None:continue
    res=rdFMCS.FindMCS([m1,mol])
    if res.numAtoms ==m1.GetNumAtoms() and res.numAtoms ==mol.GetNumAtoms():
        print(mol.GetNumAtoms())
        print (Chem.MolToSmiles(mol))


inf7=open(r'C:\Users\admin\PycharmProjects\temp\Data7.sdf')
fsuppl7=Chem.ForwardSDMolSupplier(inf7)
m=0
for mol in fsuppl2:
    print(mol.GetNumAtoms())
    print (Chem.MolToSmiles(mol))