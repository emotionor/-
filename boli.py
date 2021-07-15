import numpy as np
import math


class bolineng(object):
    """docstring for bolineng"""
    def __init__(self, filename):
        self.filename = filename 
        self.atmtyp     = []
        self.elenu      = []
        self.structure  = []
        self.lattice    = []
        self.positions  = []
        self.numbers    = []

    def read_poscar(self):
        try:
            with open(self.filename, "r") as f:
                file = f.readlines()
        except FileNotFoundError:
            print("Not find %s"%filename)
            sys.exit(0)
    
        lists = []
    
        for a in [2, 3, 4]:
            row = []
            for b in file[a].split():
                row.append(float(b))
            lists.append(row)
        self.lattice = np.array(lists) * float(file[1])

        self.atmtyp  = file[5].strip().split()
        self.elenu   = file[6].split()

        self.numbers = sum([int(a) for a in self.elenu])
    
        self.positions = []
        for a in range(8, 8 + self.numbers):
            row = []
            for b in file[a].split():
                row.append(float(b))
            self.positions.append(row)
    
        self.structure = (self.lattice, self.positions, self.numbers)

    def transf_M(self, resM):
        return '\n'.join('\t'.join([str( '{:.8f}'.format(round(x, 8))) for x in row]) for row in resM)+'\n'

    def transf_L(self, resL):
        return '\t'.join([str(x) for x in resL])+'\n'

    def bolid(self, d, lists):
        self.newpositions = self.positions
        self.newlattice = self.lattice
        for i in lists:
            self.newpositions[i-1][2] = d + self.positions[i-1][2]
        self.newlattice[2][2] = d + self.lattice[2][2]


    def write_poscar(self, poscarname):
        f = open(poscarname, "w")
        f.write("header\n")
        f.write("1.0\n")
        f.write(self.transf_M(self.lattice))
        f.write(self.transf_L(self.atmtyp))
        f.write(self.transf_L(self.elenu))
        f.write("Cartesian\n")
        f.write(self.transf_M(self.positions))

a = bolineng("CONTCAR.vasp")
a.read_poscar()
#print(a.positions[1][3])
a.bolid(2, [2, 7])
a.write_poscar("POSCAR")