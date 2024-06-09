import random
import string
import os
import time

def generate_random_char():
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters
    # Randomly choose characters from letters for the given length of the string
    random_string = ''.join(random.choice(letters))
    return random_string

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            if j == 0:
                print('.',end='')
            else:
                print(j,end='')
            print(' ',end='')
            
        print('') 

 

def cubify(matrix,row,column):
    y_center = int(len(matrix)*2/3)
    x_center = int(len(matrix)/5)
    for i in range(row):
        for j in range(column):
            if i == row-1 or j == column-1 or ((i+row) ==row) or ((j+column)==column):
                matrix[y_center-i][x_center+j] = generate_random_char()
    
    limit = int(row/2)
    for i in range(limit):
        matrix[y_center-row-i+1][x_center+column+i-1] = generate_random_char()
        matrix[y_center-row-i+1][x_center+i] = generate_random_char()
        matrix[y_center-i][x_center+column+i-1] = generate_random_char()


    for i in range(column):
        matrix[y_center-row-limit+1][x_center+i+limit] = generate_random_char()
    for i in range(row):
        matrix[y_center-i-limit][x_center+column+limit-1] = generate_random_char()




for i in range(10):
    os.system('cls')
    rows, cols = (30, 30)
    matrix =[[0 for i in range(cols)] for j in range(rows)]
    reverse = 10-i
    cubify(matrix,reverse,reverse)
    print_matrix(matrix)
    time.sleep(.1)
        














'''
def generate_rotate_pyramid():
        rotate = .triangle_3d*100
        while(True):
            os.system('cls')
            .graph= [[0 for i in range(50)] for j in range(50)]
            rotate = rotate.dot(.rotate_y)
            rotate = rotate.dot(.rotate_x)
            rotate = rotate.dot(.rotate_z)
            new_triangle = rotate.dot(.projection)
            line = []
            line += (.connect_points(new_triangle[0][0],new_triangle[0][1],new_triangle[1][0],new_triangle[1][1]))
            line += (.connect_points(new_triangle[1][0],new_triangle[1][1],new_triangle[2][0],new_triangle[2][1]))
            line += (.connect_points(new_triangle[2][0],new_triangle[2][1],new_triangle[3][0],new_triangle[3][1]))
            line += (.connect_points(new_triangle[3][0],new_triangle[3][1],new_triangle[0][0],new_triangle[0][1]))
            
            line += (.connect_points(new_triangle[0][0],new_triangle[0][1],new_triangle[4][0],new_triangle[4][1]))
            line += (.connect_points(new_triangle[1][0],new_triangle[1][1],new_triangle[4][0],new_triangle[4][1]))
            line += (.connect_points(new_triangle[2][0],new_triangle[2][1],new_triangle[4][0],new_triangle[4][1]))
            line += (.connect_points(new_triangle[3][0],new_triangle[3][1],new_triangle[4][0],new_triangle[4][1]))
            '''