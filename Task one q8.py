import csv
def cones():
    f=open("cones.csv","w",newline="")
    wobj=csv.writer(f)
    wobj.writerow(["Cone ID","x","y","Colour"])
    n=int(input("Enter number of rows to input"))
    i=0
    while i<n:
        c=int(input("Enter Cone ID:"))
        x=int(input("Enter x coordinate:"))
        y=int(input("Enter y coordinate:"))
        col=input("Enter colour:")
        L=[c,x,y,col]
        if col.lower() !="blue" and col.lower() !="yellow":
            print("Invalid input")
            continue
        else:
            wobj.writerow(L)
            i+=1
    f.close()

def distance():
    f=open("cones.csv","r",newline="")
    robj=csv.reader(f)
    header=next(robj)
    rows=list(robj)
    rows=[row for row in rows if len(row)=4]
    rows.sort(key=lambda point:(int(point[1])**2+int(point[2])**2))
    
    f1=open("cones.csv","w",newline="")
    wobj1=csv.writer(f1)
    wobj1.writerow(header)
    wobj1.writerows(rows)

    for row in rows:
        print(row)
    f.close()
    f1.close()

def colour():
    f=open("cones.csv","r",newline="")
    f1=open("conesyellow.csv","w",newline="")
    f2=open("conesblue.csv","w",newline="")
    reader=csv.reader(f)
    writer1=csv.writer(f1)
    writer2=csv.writer(f2)
    header=next(reader)
    writer1.writerow(header)
    writer2.writerow(header)
    for row in reader:
        if row[3].lower()=="yellow":
            writer1.writerow(row)
        else:
            writer2.writerow(row)
    f.close()
    f1.close()
    f2.close()

def nearest():
    f=open("centerline.csv","w",newline="")
    f1=open("conesyellow.csv","r",newline="")
    f2=open("conesblue.csv","r",newline="")
    reader1=csv.reader(f1)
    reader2=csv.reader(f2)
    next(reader1)
    next(reader2)
    wobj=csv.writer(f)
    yellow=list(reader1)
    blue=list(reader2)
    for row in blue:
        bx=int(row[1])
        by=int(row[2])
        nearest=min(yellow, key=lambda point:(bx-int(point[1]))**2 + (by-int(point[2]))**2)
        yx=int(nearest[1])
        yy=int(nearest[2])
        mx = (bx + yx)/2
        my = (by + yy)/2
        wobj.writerow([mx, my])
    f.close()
    f1.close()
    f2.close()
    f3=open("centerline.csv","r")
    reader=csv.reader(f3)
    for r in reader:
        print(r)
    f3.close()


cones()
distance()
colour()
nearest()


    
    
        
