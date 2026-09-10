n=int(input("Enter integer:"))
L=[]
for i in range(n):
    s=input("Enter string:")   
    L.append(s)
k=[]
v=[]
c=0
for i in L:
    for j in i:
        if j.lower() not in k:
            k.append(j.lower())
for a in k:
    c=0
    for b in L:
        for d in b:
            if d.lower()==a:
                c+=1
    v.append(c)            
d=dict(zip(k,v))
print(d)
        