import random
from copy import deepcopy

class Matrix:
    def __init__(self,rows,cols):
        self.n = rows
        self.m = cols
        self.table = []
        
        for i in range(self.n):
            self.table.append([0]*int(self.m))
            
        for j in range(self.n):
            for k in range(self.m):
                self.table[j][k] = random.randint(0,9)


    def fun(self,x):
        obj = Matrix(len(x),len(x[0]))
        for i in range(len(x)):
            for j in range(len(x[0])):
                obj.table[i][j] = x[i][j]

        return obj

    
#add
    def add(self, z):
        self.add = []
        for i in range(self.n):
            self.add.append([0]*int(self.m))

        for i in range(self.n):
            for j in range(self.m):
                self.add[i][j] = self.table[i][j]+z.table[i][j]

        return self.fun(self.add)

#sub
    def sub(self,z):
        self.sub = []
        for i in range(self.n):
            self.sub.append([0]*int(self.m))

        for i in range(self.n):
            for j in range(self.m):
                self.sub[i][j] = self.table[i][j]-z.table[i][j]

        return self.fun(self.sub)

#mul
    def mul(self,z):
        self.mul = []
        for i in range(self.n):
            self.mul.append([0]*int(z.m))
        for i in range(len(self.table)):
            for j in range(len(z.table[0])):
                for k in range(len(z.table)):
                    self.mul[i][j] += self.table[i][k]*z.table[k][j]
      
        return self.fun(self.mul)

#trans
    def trans(self) :
        self.trans = []
        for k in range(self.m):
            self.trans.append([0]*int(self.n))
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                self.trans[j][i] = self.table[i][j]

        return self.fun(self.trans)

#display
    def display(self):
        for i in self.table:
            for j in i:
                print(j, end="\t")
            print()



a = Matrix(int(input("Enter the rows of A matrix:")),int(input("Enter the columns of A matrix:")))
a.display()
b = Matrix(int(input("Enter the rows of B matrix:")),int(input("Enter the columns of B matrix:")))
b.display()

print('----------A+B-----------')
try:
    c = a.add(b)
    c.display()
except:
    print("Matrixs' size should be in the same size")
    
print('----------A-B-----------')
try:
    e = a.sub(b)
    e.display()
except:
    print("Matrixs' size should be in the same size")
    
print('----------A*B-----------')

try:
    d = a.mul(b)
    d.display()
except:
    print("Matrixs are not multable")
print('--The transpose of A*B--')

try:
    d = a.mul(b)
    f = d.trans()
    f.display()
except:
    print("A*B Matrix doesn't exit")
