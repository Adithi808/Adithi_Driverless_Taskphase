def open_hash():
    l=[[],[],[],[],[],[],[],[],[],[]]
    n=int(input("Enter number of integers to input:"))
    for i in range(1,n+1):

        num=int(input(f"Enter integer{i}:"))
        r=num%10
        l[r].append(num)
    for i in l:
        print(i,end="")
open_hash()


