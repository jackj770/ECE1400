# Jack Fernald
# Assignment: Matrix_Multiplication
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on January 25, 2022
import sys

mat1 = []
mat2 = []
matresult = []


def creatematricies(m, n, p):
    print("Creating matrix %i x %i" % (m, n))
    for ii in range(m):  # Row in Matrix A
        temp = []
        for jj in range(n):  # Element in row in Matrix A
            try:
                temp.append(int(input("Enter element A[%i][%i]: " % (ii, jj))))
            except ValueError:
                print("Whoops, that doesn't seem to work... Try again")
                temp.append(int(input("Enter element A[%i][%i]: " % (ii, jj))))
        mat1.append(temp)
        # print("appending")
    print("Creating matrix %i x %i" % (n, p))
    for ii in range(p):  # Column in Matrix B
        temp = []
        for jj in range(n):  # Element in column in Matrix A
            temp.append(int(input("Enter element B[%i][%i]: " % (jj, ii))))
        mat2.append(temp)


def multiply(m, n, p):
    running = 0
    for ii in range(m):  # Iterate over A rows
        m1temp = mat1[ii]
        temp = []
        for jj in range(p):  # Iterate over B columns
            m2temp = mat2[jj]
            for kk in range(n):  # Iterate over B row and A columns
                running = m1temp[kk] * m2temp[kk] + running
            temp.append(running)
            running = 0
        matresult.append(temp)


try:
    creatematricies(int(sys.argv[1]), int(sys.argv[2]), int((sys.argv[3])))
except IndexError:
    print("Unexpected value. Plese Type <m> <n> <p> with your desired values.")
    exit()
try:
    multiply(int(sys.argv[1]), int(sys.argv[2]), int((sys.argv[3])))
    for ii in range(int(sys.argv[3])):
        print(matresult[ii])
except IndexError:
    print("Unexpected value. Please Type <m> <n> <p> with your desired values.")
    exit()
