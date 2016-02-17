import math

class countinteger:
    def count(self,no):
        count=0
        while(no>=10):
            count=count+1
            no=no/10
        count=count+1
        return count
    def firstdigit(self,n):
        while(n>=10):
            n=n/10
        return n

class normaliser:
    def __init__(self,arr):

        self.ce=countinteger()
        self.array=arr
        #arr=[[1,2],[3,4]]
        self.row=len(arr)
        self.col=len(arr[0])
        self.y=[]
        #self.A=arr[0][0]

#normalization procedure calculation
    def normalizematrix(self):
        for i in range(0,self.row):
            self.y.append([])
            for j in range(0,self.col):
                n=self.ce.count(self.array[i][j])
                x=self.array[i][j]
                A=self.ce.firstdigit(x)
                temp=n-1
                te=math.pow(10,temp)
                res=((x)-(te*A))/te
                self.y[-1].append(res)

        return self.y