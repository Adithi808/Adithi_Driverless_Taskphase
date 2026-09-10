def matrix_multiplication():
    n=int(input("Enter number of rows for matrix 1:"))
    m=int(input("Enter number of columns for matrix 1:"))
    p=int(input("Enter number of rows for matrix 2:"))
    q=int(input("Enter number of columns for matrix 2:"))
    if m!=p:
        print("Multiplication not possible")
        return
    #Creating matrix 1
    matrix1=[]
    matrix2=[]
    result=[]
    #Create result matrix
    for i in range(n):
         l=[]
         for j in range(q):
              l.append(0)
         result.append(l)
    #Creating matrix 1
    for i in range(n):
        L=[]
        for j in range(m):
            v=int(input("Enter values for matrix1:"))
            L.append(v)
        matrix1.append(L)
    #Creating matrix 2
    for i in range(p):
            L=[]
            for j in range(q):
                v=int(input("Enter values for matrix2:"))
                L.append(v)
            matrix2.append(L)
    #Multiplication
    for i in range(n):   #for rows
         for j in range(q): #for columns
              result[i][j]=0
              for k in range(p): #each element (common)
                   result[i][j]+=matrix1[i][k]*matrix2[k][j]
    print(result)
matrix_multiplication()
                   
         

    
    
