import math
from matrixformer import matrixcomputation
from attributecalc import multiattribute
from normalizer import normaliser
from weightcalulator import weightcalc
import matplotlib.pyplot as plt
class mainframe:

    def __init__(self):

        self.ma=matrixcomputation()
        self.array=self.ma.matcom()
        self.array2=self.ma.cloud2()
        self.array3=self.ma.cloud3()
        #print self.array
        #print self.array2
        #print self.array3
        self.aa=multiattribute()
        self.matr=self.aa.matrix(self.array,self.array2,self.array3)
        #print self.matr

        #m=mainframe()
        self.no=normaliser(self.matr)
        self.normatrix=self.no.normalizematrix()
#print normatrix
        self.g=weightcalc()
        self.we=self.g.attributecalc(self.normatrix)
        m=len(self.we)
        self.T=[]
        for i in range(0,3):
            self.T.append([])
            for j in range(0,6):
                temp=self.normatrix[i][j]*self.we[j]
                self.T[-1].append(temp)

    def printplot(self):
        for row in self.T:
            for val in row:
                print val
            print '\n'

    def plotgraph(self):
        plt.plot([1,2,3,4,5,6],self.T[0], 'ro')
        plt.axis([0, 6, 0, 1])
        plt.ylabel('trust weight')
        plt.xlabel('resource attributes')
        plt.show()
        plt.plot([1,2,3,4,5,6], self.T[1], 'ro')
        plt.axis([0, 6, 0, 1])
        plt.ylabel('trust weight')
        plt.xlabel('resource attributes')
        plt.show()
        plt.plot([1,2,3,4,5,6], self.T[2], 'ro')
        plt.axis([0, 6, 0, 1])
        plt.ylabel('trust weight')
        plt.xlabel('resource attributes')
        plt.show()






