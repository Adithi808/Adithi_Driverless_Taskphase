class selectionsort:
    def __init__(self):
        self.L=[]
    def create_list(self):
        n=int(input("Enter integer:"))
        self.L=[]
        for i in range(n):
            s=input("Enter string:")   
            self.L.append(s)



    def selection_sort(self):
        for i in range(len(self.L)):
            min=i
            for j in range(i+1,len(self.L)):
                if self.L[j]<self.L[min]:
                    min=j
            temp=self.L[i]
            self.L[i]=self.L[min]
            self.L[min]=temp
        print(self.L)
obj=selectionsort()
obj.create_list()
obj.selection_sort()
            
                    
                




