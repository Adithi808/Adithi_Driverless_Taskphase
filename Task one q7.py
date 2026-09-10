def sorting():
    ref=eval(input("Enter reference coordinates:"))
    n=int(input("Enter no of coordinates to be entered:"))
    L=[]
    for i in range(n):
        c=eval(input("Enter coordinates:"))
        L.append(c)
    return sorted(L,key=lambda point:(point[0]-ref[0])**2+(point[1]-ref[1])**2)
print(sorting())


