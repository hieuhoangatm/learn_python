class CC:
    def __init__(self,id,ten,lop):
        self.id=id
        self.ten=ten
        self.lop=lop
t=int(input())
t1=t
a=[]
while(t>0):
    t-=1
    a.append(CC(input(),input(),input()))
m={}
while(t1>0):
    t1-=1
    x,y=map(str,input().split())
    for i in a:
        if i.id==x:
            diem=10
            for j in y:
                if j=='m':
                    diem-=1
                if j=='v':
                    diem-=2
                if diem<=0:
                    diem=0
                    break
            i.d=diem
            if diem ==0:
                i.gc="KDDK"
            else:
                i.gc=""
for i in a:
    print(i.id,i.ten,i.lop,i.d,i.gc)