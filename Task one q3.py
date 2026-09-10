class binarysearch:
    def __init__(self):
            self.L=[]
    def create_list(self):
        n=int(input("Enter integer:"))
        self.L=[]
        for i in range(0,n):
            s=input("Enter string:")   
            self.L.append(s)
    
    
    
    def selection_sort(self):
        for i in range(len(self.L)):
            min=self.L[i]
            for j in range(i+1,len(self.L)):
                if self.L[j]<min:
                    min=self.L[j] 
                    temp=self.L[i]
                    self.L[i]=min
                    self.L[j]=temp
        print(self.L)


    def binary_search(self):
        str=input("Enter string to search for:")
        low=0
        high=len(self.L)-1
        while low<=high:
            mid=(low+high)//2
            if self.L[mid]==str:
                print("String found at index:",mid)
                break
            elif self.L[mid]>str:
                high=mid-1
            else:
                low=mid+1
        else:
            print("String not found")
obj=binarysearch()
obj.create_list()
obj.selection_sort()
obj.binary_search()


    
            