import MySQLdb as mys
import getpass
import sys
from mainframe import mainframe
class minweight:
    def maximum(self,a,b,c):
        if(a>b):
            if(a>c):
                return 1
            else:
                return 3
        elif(b>a):
            if(b>c):
                return 2
            else:
                return 3
        elif(c>a):
            if(c>b):
                return 3
            else:
                return 2
db=mys.connect('localhost','project','project','cloud')
cursor=db.cursor()
typ=raw_input('type login if you already have account or type signup')
if(typ=='login'):
        usernam=raw_input('enter the username')
        passwor=getpass.getpass("enter password")
        que1="select COUNT(1) from authentication where username='%s' and password='%s'" % (usernam,passwor)
        try:
            cursor.execute(que1)
            res=cursor.fetchone()[0]
        except:
            print 'error'
        if(res==1):
            print 'login sucess'
            que2="select access from authentication where username='%s' and password='%s'" % (usernam,passwor)
            cursor.execute(que2)
            res2=cursor.fetchone()[0]
            if(res2=='admin'):

                    mf=mainframe()
                    n=raw_input("enter text for values and plot for graph of the cloud result")
                    if(n=="text"):
                        mf.printplot()
                    elif(n=="plot"):
                        mf.plotgraph()



            else:

                      cpuneeded=int(raw_input("enter the cpu needed"))
                      memneeded=int(raw_input("enter the memory needed"))
                      netneeded=int(raw_input("enter the network needed"))
                      mf=mainframe()
                      mt=mf.T
                      tru=[]
                      for i in range(0,3):
                          tru.append([])
                          sum=0
                          for j in range(0,6):
                              sum=sum+mt[i][j]
                          tru[-1].append(sum)
                      mi=minweight()
                      maxi=mi.maximum(tru[0],tru[1],tru[2])
                      #print max
                      sql="select count(time) from resrources where clusterid='%d' " % \
                            (3)
                      try:
                            cursor.execute(sql)
                            res=int(cursor.fetchone()[0])
                            #print res
                      except:
                            print 'error details'


                      sql2="select * from resrources where clusterid='%d' and time='%d'" % (3,res)
                      try:
                          cursor.execute(sql2)
                          resu=cursor.fetchall()
                          for row in resu:
                              ca=int(row[2])
                              ma=int(row[3])
                              na=int(row[4])
                              cu=int(row[5])
                              mu=int(row[6])
                              nu=int(row[7])
                          print ca,ma,na,cu,mu,nu

                      except:
                          print 'error details'
                      ca=ca-cpuneeded
                      ma=ma-memneeded
                      na=na-netneeded
                      cu=cu+cpuneeded
                      mu=mu+memneeded
                      nu=nu+netneeded
                      print ca,ma,na,cu,mu,nu
                      #sql3="update resrources set cpuavail='%d' memavail='%d' netavail='%d' cpuutil='%d' memutil='%d' netutil=%d' where clusterid='%d' and time='%d' " % \
                           #(ca,ma,na,cu,mu,nu,max,res)
                      try:
                            cur=db.cursor()
                            cur.execute("UPDATE resrources SET cpuavail= %s WHERE clusterid = %s and time=%s", (ca,maxi,res))
                            cur.execute("UPDATE resrources SET memavail= %s WHERE clusterid = %s and time=%s", (ma,maxi,res))
                            cur.execute("UPDATE resrources SET netavail= %s WHERE clusterid = %s and time=%s", (na,maxi,res))
                            cur.execute("UPDATE resrources SET cpuutil= %s WHERE clusterid = %s and time=%s", (cu,maxi,res))
                            cur.execute("UPDATE resrources SET memutil= %s WHERE clusterid = %s and time=%s", (mu,maxi,res))
                            cur.execute("UPDATE resrources SET netutil= %s WHERE clusterid = %s and time=%s", (nu,maxi,res))
                            print 'resource allocated'
                            db.commit()
                      except:
                          print 'update error'
        else:

            print 'wrong credentials'

elif(typ=='signup'):
        user=raw_input("enter the username")
        passw=raw_input("enter the pass")
        que="insert into authentication values('%s','%s','%s')" % (user,passw,'user')
        try:
            cursor.execute(que)
            db.commit()
            print 'signup sucess'
        except:
            print 'error'
