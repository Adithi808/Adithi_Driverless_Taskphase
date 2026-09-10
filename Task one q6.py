def index(subl,num):
    low=0
    high=len(subl)
    while low<high:
        mid=(low+high)//2
        if subl[mid]>num:
            high=mid
        else:
            low=mid+1
    return low

def open_hash():
    l=[[],[],[],[],[],[],[],[],[],[]]
    n=int(input("Enter number of integers to input:"))
    for i in range(1,n+1):

        num=int(input(f"Enter integer{i}:"))
        r=num%10
        idx=index(l[r],num)
        l[r].insert(idx,num)
    for i in l:
        print(i)
open_hash()