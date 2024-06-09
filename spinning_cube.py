import numpy as np
import math
import time



    ######## Matrix to project onto the 2d world
projection = np.array([[1,0,0],
                        [0,1,0],
                        [0,0,0]])
    
        ######## Matrix representation of a cube
cube_3d = np.array([[-1, -1, 1], 
                            [1, -1, 1],
                            [1, 1, 1],
                            [-1, 1, 1],
                            [-1, -1, -1],
                            [1, -1, -1],
                            [1, 1, -1],
                            [-1, 1, -1]])

triangle_3d = np.array([[-1,-1,-1],
                                     [1,-1,-1],
                                     [1,-1,1],
                                     [-1,-1,1],
                                     [0,1,0]])
        ######## Graph that will have the points of the cube
        #graph= [[0 for i in range(40)] for j in range(40)]

angle = .01
rotate_y = np.array([[math.cos(angle),0,math.sin(angle)],
                            [0,1,0],
                            [math.sin(angle)*(-1),0,math.cos(angle)]])
rotate_x = np.array([[1,0,0],
                            [0,math.cos(angle),math.sin(angle*(-1))],
                            [0,math.sin(angle),math.cos(angle)]])
rotate_z = np.array([[math.cos(angle),math.sin(angle)*(-1),0],
                            [math.sin(angle),math.cos(angle),0],
                        [0,0,1]])

 

  
    
def connect_points(x1,y1,x2,y2):
    rise = y2 - y1
    run = x2 - x1
    slope = rise/run
        
    y_intercept = y1-(slope*x1)
    points=[]
    if x1 > x2:
        start = x2
        end = x1
    else:
        start = x1
        end = x2
    for i in range(int(start),int(end)):
        points.append([i,(slope*i)+y_intercept])
        

    rise = x2 - x1
    run = y2 - y1
    slope = rise/run
    x_intercept = x1-(slope*y1)
        
    if y1 > y2:
        start = y2
        end = y1
    else:
        start = y1
        end = y2
    for i in range(int(start),int(end)):
        points.append([(slope*i)+x_intercept,i])
    return points



def print_cube(line):
        
    try:
        for i in line:
                
            graph[int(25-i[0]/20)][int(25-i[1]/20)] = 'M'
    except IndexError:
        pass
    for i in graph:
        for j in i:
            if j == 0:
                print('.',end='')
            else:
                print(j,end='')
            print(' ',end='')
                    
        print('')
    
        

rotate = cube_3d*210
rotate = rotate.dot(rotate_y)

        
while True:
    
    print('\033[50A\033[2K', end='') 
    graph= [[0 for i in range(50)] for j in range(50)]
    rotate = rotate.dot(rotate_x)
    rotate = rotate.dot(rotate_y)
    rotate = rotate.dot(rotate_z)
    rotate = rotate.dot(rotate_x)
    new_cube = rotate.dot(projection)
            
    line = []
            
    line += (connect_points(new_cube[0][0],new_cube[0][1],new_cube[1][0],new_cube[1][1]))
    line += (connect_points(new_cube[1][0],new_cube[1][1],new_cube[2][0],new_cube[2][1]))
    line += (connect_points(new_cube[2][0],new_cube[2][1],new_cube[3][0],new_cube[3][1]))
    line += (connect_points(new_cube[3][0],new_cube[3][1],new_cube[0][0],new_cube[0][1]))
    line += (connect_points(new_cube[4][0],new_cube[4][1],new_cube[5][0],new_cube[5][1]))
    line += (connect_points(new_cube[5][0],new_cube[5][1],new_cube[6][0],new_cube[6][1]))
    line += (connect_points(new_cube[6][0],new_cube[6][1],new_cube[7][0],new_cube[7][1]))
    line += (connect_points(new_cube[7][0],new_cube[7][1],new_cube[4][0],new_cube[4][1]))
    line += (connect_points(new_cube[0][0],new_cube[0][1],new_cube[4][0],new_cube[4][1]))
    line += (connect_points(new_cube[1][0],new_cube[1][1],new_cube[5][0],new_cube[5][1]))
    line += (connect_points(new_cube[2][0],new_cube[2][1],new_cube[6][0],new_cube[6][1]))
    line += (connect_points(new_cube[3][0],new_cube[3][1],new_cube[7][0],new_cube[7][1]))
    
    print('\033[50A\033[2K', end='') 
    print_cube(line)
            
    time.sleep(.01)
    
 
            
            
            
            
            
            
       
