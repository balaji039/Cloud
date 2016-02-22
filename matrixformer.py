import MySQLdb as mys
import sys

class matrixcomputation:
    def __init__(self):
        self.db=mys.connect('localhost','project','project','cloud')
        self.cursor=self.db.cursor()
    def matcom(self):
        que="select count(time) from resrources where clusterid=1"
        try:
            self.cursor.execute(que)
            n=self.cursor.fetchone()[0]
            j=1
            arr=[]
            for i in range(0,6):
                que2="select * from resrources where clusterid=1"
                self.cursor.execute(que2)
                res=self.cursor.fetchall()
                j=j+1
                arr.append([])
                for row in res:
                    #print row[j]
                    arr[-1].append(int(row[j]))
            #print arr
        except:
            print 'error'
        return arr

    def cloud2(self):
        #arr = []
        que="select count(time) from resrources where clusterid=1"
        try:
            self.cursor.execute(que)
            n=self.cursor.fetchone()[0]
            j=1
            arr2=[]
            for i in range(0,6):
                que2="select * from resrources where clusterid=2"
                self.cursor.execute(que2)
                res=self.cursor.fetchall()
                j=j+1
                arr2.append([])
                for row in res:
                    #print row[j]
                    arr2[-1].append(int(row[j]))
            #print arr
        except:
            print 'error'
        return arr2

    def cloud3(self):
        #arr = []
        que="select count(time) from resrources where clusterid=1"
        try:
            self.cursor.execute(que)
            n=self.cursor.fetchone()[0]
            j=1
            arr3=[]
            for i in range(0,6):
                que2="select * from resrources where clusterid=3"
                self.cursor.execute(que2)
                res=self.cursor.fetchall()
                j=j+1
                arr3.append([])
                for row in res:
                    #print row[j]
                    arr3[-1].append(int(row[j]))
            #print arr
        except:
            print 'error'
        return arr3