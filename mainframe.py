from matrixformer import matrixcomputation
from attributecalc import multiattribute
from normalizer import normaliser
from weightcalulator import weightcalc

class mainframe:

    def __init__(self):

        self.ma=matrixcomputation()
        self.array=self.ma.matcom()
        self.array2=self.ma.cloud2()
        self.array3=self.ma.cloud3()
        self.aa=multiattribute()
        self.matr=self.aa.matrix(self.array,self.array2,self.array3)


m=mainframe()
no=normaliser(m.matr)
normatrix=no.normalizematrix()
print normatrix
g=weightcalc()
we=g.attributecalc(normatrix)

