#Hamza Iqbal COT4500 Assignment 2
#February 20th, 2023 
#Covers the entirety of Chapter 3

import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


#QUESTION 1: Using Neville’s method, find the 2nd degree interpolating value for f(3.7) for the following set of data 

def neville_method(x_points, y_points, x_values):
    x_points = [3.6, 3.8, 3.9] 
    y_points = [1.675, 1.436, 1.318] #the interpolating values 

    matrix = np.zeros((3,3))

    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]

    value = x_values
    num_of_points = len(x_points)
    for i in range(1,num_of_points):
            for j in range(1, i + 1):
                first_multiplication = (value - x_points[i-j]) * matrix[i][j-1]
                second_multiplication = (value - x_points[i]) * matrix[i-1][j-1]

                denominator = x_points[i] - x_points[i-j]

                coefficient = (first_multiplication - second_multiplication)/denominator

                matrix[i][j] = coefficient


    print(matrix[num_of_points - 1][num_of_points - 1])



if __name__ == "__main__": 
    x_points = []
    y_points = []
    approximating_value = 3.7 #the value we are trying to solve

    neville_method(x_points, y_points, approximating_value)


#QUESTION 2: Using Newton’s forward method, print out the polynomial approximations for degrees 1, 2, and 3 using the following set of data

p1 = (25.3913-23.5492) / (7.4-7.2)
q1 = (26.8224-25.3913) / (7.5-7.4)
k1 = (27.4589-26.8224) / (7.6-7.5)

p2 = (q1-p1) / (7.5-7.2)
q2 = (k1-p1) / (7.6-7.4)

p3 = (q2-p2) / (7.6-7.2)
print([p1, p2, p3])


#QUESTION 3: Using the results from 3, approximate f(7.3)? 

p1x = 23.5492 + p1*(7.3-7.2)
p2x = p1x + p2*(7.3-7.4)*(7.3-7.2)
p3x = p2x + p3*(7.3-7.5)*(7.3-7.4)*(7.3-7.2)
print(p3x)


#QUSETION 4: Using the divided difference method, print out the Hermite polynomial approximation matrix


#print each value out two times
x1 = 3.6
x2 = 3.6
x3 = 3.8
x4 = 3.8
x5 = 3.9
x6 = 3.9

y1 = 1.675
y2 = 1.675
y3 = 1.436
y4 = 1.436
y5 = 1.318
y6 = 1.318

d1 = 0 
d2 = -1.195
d3 = round((y3 - y2) / (x3 - x2), 7)
d4 = -1.188
d5 = round((y5-y4) / (x5-x4), 7)
d6 = -1.182

xx1 = 0
xx2 = 0
xx3 = round((d3-d2) / (x3-x2), 7)
xx4 = round((d4-d3) / (x4-x2), 7)
xx5 = round((d5-d4) / (x5-x3), 7)
xx6 = round((d6-d5) / (x6-x4), 7)

yy1 = 0
yy2 = 0
yy3 = 0
yy4 = round((xx4-xx3) / (x4-x1), 7)
yy5 = round((xx5-xx4) / (x5-x2), 7)
yy6 = round((xx6-xx5) / (x6-x3), 7)

dd1 = 0 
dd2 = 0
dd3 = 0
dd4 = 0
dd5 = round((yy5-yy4) / (x5-x1), 7)
dd6 = round((yy6-yy5) / (x6-x2), 7)

hermite = np.matrix([[x1,y1,d1,xx1,yy1,dd1],[x2,y2,d2,xx2,yy2,dd2],[x3,y3,d3,xx3,yy3,dd3], [x4,y4,d4,xx4,yy4,dd4], [x5,y5,d5,xx5,yy5,dd5], [x6,y6,d6,xx6,yy6,dd6]]) 
print(hermite)

#QUESTION 5: Using cubic spline interpolation, solve for the following using this set of data: Matrix A, Vector b, and Vector X


x = [2, 5, 8, 10]
y = [3, 5, 7, 9]
length = len(x)
z = np.zeros(length - 1)
d = np.zeros(length)
for row in range(length - 1):
    z[row] = x[row + 1] - x[row]
    d[row + 1] = (y[row + 1] - y[row]) / z[row]

A = np.zeros((length, length))
b = np.zeros(length)
for row in range(1, length - 1):
    A[row][row - 1] = z[row - 1]
    A[row][row] = 2 * (z[row - 1] + z[row])
    A[row][row + 1] = z[row]
    b[row] = 3 * (d[row + 1] - d[row])

A[0][0] = 1
A[length - 1][length - 1] = 1

x = np.linalg.solve(A, b)
print("")
print(A)
print("")
print(b)
print("")
print(x)





