import random
from collections import Counter
class node:
    def __init__(self):
        self.label = -1
        self.count = 1
        self.userid = -1
        self.password = -1
        self.username = "a"



class graph:
    def __init__(self):
        with open("names.txt") as dict:
            dict1 = dict.read().split('\n')
        self.n = int(input("no of vertices"))
        self.m = int(input("no of egdes"))
        self.l = [0] * (self.n)
        self.d=[0] *(self.n)
        self.nv = [0] * (self.n)
        self.state = 1
        for i in range(self.n):
            self.l[i] = []
            self.nv[i] = node()
            self.nv[i].label = i
            self.nv[i].username=dict1[i]
            self.nv[i].userid=i
            self.nv[i].password=i
            self.d[i] = i

        print("enter the edges")
        for i in range(self.m):
            j = int(input())
            k = int(input())
            self.l[j-1].append(k-1)
            self.l[k-1].append(j-1)

    def maximal_checker(self, v, b):
        cl = self.nv[v].label
        al = [-1] * (len(self.l[v]))
        for i in range(len(self.l[v])):
            ad = self.l[v][i]
            al[i] = self.nv[ad].label
        if len(al)!=0:
            count = Counter(al)
            me = count.most_common()[0][0]
            mc = count.most_common()[0][1]
            if (b == 0):
                if (mc==1):
                    if(cl==self.nv[self.l[v][0]].label):
                        return True
                    else:
                        return False
                if (self.nv[v].count == mc):
                    return True

                return False

            if (b == 1):
                self.nv[v].label = me
                self.nv[v].count = mc


    def entire_checker(self):
        random.shuffle(self.d)
        for i in range(self.n):
            vn = self.d[i]
            x = self.maximal_checker(vn, 0)
            if (x == False):
                return False
        return True


    def lpa(self):
        x=False
        t=0
        while( x == False ):
            t=t+1
            x = self.entire_checker()
            for i in range(self.n):
                vn = self.d[i]
                self.maximal_checker(vn, 1)




    def printer(self):
        for i in range(self.n):
            print(i, "label************************************************")
            for j in range(self.n):
                if (i == self.nv[j].label):
                    print(j+1)

    def suggestion(self,k):
        cl=self.nv[k].label
        for i in range(self.n):
            if (i!=k):
                if(self.nv[i].label == cl):
                    if(not(self.nv[i].userid in self.l[k])):
                        print(self.nv[i].username,+self.nv[i].userid)




    def register(self):
        print(" WELCOME to REGISTER page")
        n=input("enter username")
        p=input("enter password")
        self.l.append(0)
        self.nv.append(0)
        self.n=self.n+1
        k=self.n-1
        self.l[k]=[]
        self.nv[k]=node()
        self.nv[k].username = n
        self.nv[k].userid=k
        self.nv[k].password=p
        n=int(input("no of friends u know"))
        print("enter your friends id")
        for i in range(n):
            j=int(input())
            self.l[k].append(j)
            self.l[j].append(k)
        self.maximal_checker(k,1)

    def login(self):
        print(" WELCOME to Login page")
        u = int(input("enter userid"))
        p = input("enter password")
        if ( self.nv[u].password == p ):
            self.suggestion(u)




G = graph()
G.lpa()
G.printer()
x=True
n=int(input("Enter 1.Registering new user, 2.Login and 3.Exit"))
while x==True:
    if(n==1):
        G.register()
    if(n==2):
        G.login()

    if(n==3):
        break
    n = int(input("Enter 1.Registering new user, 2.Login and 3.Exit"))
