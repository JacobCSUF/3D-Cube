import numpy as np
import math
import time
from numpy.linalg import norm
lighting= np.array([1,-1,0])
##### projection onto 2d
projection = np.array([[1,0,0],
                        [0,1,0],
                        [0,0,0]])
angle = .03
y = np.array([[math.cos(angle),0,math.sin(angle)],
                            [0,1,0],
                            [math.sin(angle)*(-1),0,math.cos(angle)]])
x = np.array([[1,0,0],
                            [0,math.cos(angle),math.sin(angle*(-1))],
                            [0,math.sin(angle),math.cos(angle)]])
z = np.array([[math.cos(angle),math.sin(angle)*(-1),0],
                            [math.sin(angle),math.cos(angle),0],
                        [0,0,1]])

##### Creating all x,y,z coords for cube
f1,f2,f3,f4,f5,f6 = [],[],[],[],[],[]

for i in range(-12,12):
    for j in range(-12,12):
        f1.append([i,j,12])
        f2.append([i,j,-12])
        f3.append([12,i,j])
        f4.append([-12,i,j])
        f5.append([i,12,j])
        f6.append([i,-12,j])
        
f1,f2,f3,f4,f5,f6 = np.array(f1),np.array(f2),np.array(f3),np.array(f4),np.array(f5),np.array(f6)




graph= [[[0,0] for i in range(50)] for j in range(50)]
def rotate_y():
    global f1,f2,f3,f4,f5,f6
    f1 = f1.dot(y)
    f2 = f2.dot(y)
    f3 = f3.dot(y)
    f4 = f4.dot(y)
    f5 = f5.dot(y)
    f6 = f6.dot(y)

def rotate_z():
    global f1,f2,f3,f4,f5,f6
    f1 = f1.dot(z)
    f2 = f2.dot(z)
    f3 = f3.dot(z)
    f4 = f4.dot(z)
    f5 = f5.dot(z)
    f6 = f6.dot(z)
def set_print(points,char):
    
        for i in points:
            try:
                if graph[int(20-i[0])][int(20-i[1])][0] == 0:
                    graph[int(20-i[0])][int(20-i[1])] = [char,(i[2])]
                
                elif graph[int(20-i[0])][int(20-i[1])][1] < (i[2]):
                    graph[int(20-i[0])][int(20-i[1])] = [char,(i[2])]
            except IndexError:
                pass
    
def printer():
    for i in range(len(graph)):
        
        for j in range(len(graph[i])):
           
            if graph[i][j][0] == 0:
                

                print(' ',end='')
            else:
                if graph[i][j+1][0] == graph[i][j-1][0]:
                    graph[i][j][0] = graph[i][j-1][0]
                    print(graph[i][j][0],end='')
                    
                else:
                    print(graph[i][j][0],end='')
            print(' ',end='')
        print('')



while(True):
    rotate_y()
  
    rotate_z()
    print('\033[50A\033[2K', end='') 
    set_print(f1,'.')
    set_print(f2,'!')
    set_print(f3,'=')
    set_print(f4,'~')
    set_print(f5,';')
    set_print(f6,'$')
    printer()
    time.sleep(.01)
    graph = [[[0,0] for i in range(50)] for j in range(50)]