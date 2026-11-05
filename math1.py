import numpy as np 
x0, y0 = 10.0, 5.0        # keep the initial position
x, y = x0, y0             # these get updated by the loop
x = 10.0
y = 5.0
H1=np.deg2rad(30)
T=0.2 
u=5.0
a=1.0
w=np.deg2rad(10)
H= H1+w*T  # calculating the final heading 
dt = 0.001
N = int(T/dt)
for i in range(N):  # loop is used to divide 0.2s into 200 parts
    t=i*dt  # used to calculate the time interval  
    v = u+a*t # change in velocity where v is the speed at that time
    H2 = H1+w*t     #change in heading where H2 is the heading at that time
    # both v and H2 are inside loop because we need them for each time interval 
    vx = v*np.cos(H2)   
    vy = v*np.sin(H2) 
    x =x+vx*dt  # we do dt here bc we are adding only the distance covered by the car in the next interval and not from the start 
    y =y+vy*dt    
print("New x :",x)
print("New y: ",y)
print("New heading: ",np.rad2deg(H),"degree")
def global_to_car(points, pose):
    px, py, th = pose
    R = np.array([[ np.cos(th), np.sin(th)],
                  [-np.sin(th), np.cos(th)]])
    return (points - [px, py]) @ R.T

cones = np.array([[12, 7], [8, 6], [13, 4], [9, 3]], dtype=float)  # B1, B2, Y1, Y2

pose0 = (x0, y0, H1)   # initial pose (H1 is in radians)
pose1 = (x, y, H)      # new pose from your loop (H is in radians)

print(global_to_car(cones, pose0))
print(global_to_car(cones, pose1))