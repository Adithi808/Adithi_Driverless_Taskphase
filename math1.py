import numpy as np 
x0, y0 = 10.0, 5.0       
x, y = x0, y0            
x = 10.0
y = 5.0
H1=np.deg2rad(30)
T=0.2 
u=5.0
a=1.0
w=np.deg2rad(10)
H= H1+w*T  
dt = 0.001
N = int(T/dt)
for i in range(N):  
    t=i*dt  
    v = u+a*t
    H2 = H1+w*t     
    
    vx = v*np.cos(H2)   
    vy = v*np.sin(H2) 
    x =x+vx*dt  
    y =y+vy*dt    
print("New x :",x)
print("New y: ",y)
print("New heading: ",np.rad2deg(H),"degree")
def global_to_car(points, pose):
    px, py, th = pose
    R = np.array([[ np.cos(th), np.sin(th)],
                  [-np.sin(th), np.cos(th)]])
    return (points - [px, py]) @ R.T

cones = np.array([[12, 7], [8, 6], [13, 4], [9, 3]], dtype=float)  

pose0 = (x0, y0, H1)   
pose1 = (x, y, H)      

print(global_to_car(cones, pose0))
print(global_to_car(cones, pose1))