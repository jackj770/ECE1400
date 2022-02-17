## Add stuff about file from Ubuntu

# will have the following funcitons
# Error checking functions:
# TODO: Square check
# TODO: 1D Check
# TODO: Inner dimensions check
# TODO: Same size check
# Dimension check
# Output Functions:
# Initialize with input of matrix , no shape requirements
# override print statement
# return size
# Math Functions:
# TODO: element wise addition
# TODO: Element wise subtraction
# TODO: element wise multiplication
# TODO: Matrix Multiplcation
# Extra Functions
# TODO: Trace
# TODO: Vector Norm, 1D check
# TODO: Reshape

import math

import matrix


class Matrix:
    """
    Creates an object for working with lists as matricies
	- Uses +, -, *, /, @
    """
    def __init__(self, userMatrix):
        """ 
        Initializes Matrix object
        Parameters
        ----------
        userMatrix : A list of Lists

        returns
        -------
        Nothing
        """
        self.array = userMatrix
        self.userMatrix = userMatrix
        self.mlen = len(userMatrix)
        if isinstance(self.userMatrix[0], list):
            self.nlen = len(self.userMatrix[0])
            self.__diemension_check__()
        else:
            self.nlen = 1
        self.shape = self.mlen, self.nlen
        self.size = self.mlen * self.nlen

    def __square_check__(self):
        if self.mlen != self.nlen:
            raise ValueError("row dimensions are inconsistent")

    def __oned_check__(self):
        if self.nlen > 1:
            raise ValueError("row dimensions are inconsistent")

    def __diemension_check__(self):
        for m in range(0, self.mlen):
            if len(self.userMatrix[m]) != len(self.userMatrix[0]):
                raise ValueError("row dimensions are inconsistent")

    def __repr__(self):
        """ Prints a formatted output of the Matrix object

        returns
        -------
        str
            The formatted matrix string
        """
        printed_matrix = ""
        for m in range(0, self.mlen):
            printed_matrix += "| "
            for n in range(0, self.nlen):
                self.userMatrix[m][n] = format(self.userMatrix[m][n], '.2f')
                printed_matrix += str(self.userMatrix[m][n]) + " "
            printed_matrix += "|\n"
        return printed_matrix

    def __add__(self, other):
        """ Adds two Matrix objects
        Parameters
        ----------
        other : Another Matrix object that has the same dimensions

        returns
        -------
        Matrix Object
            The summation of the two passed Matrix objects
        """
        if self.mlen != other.mlen or self.nlen != other.nlen:
            raise ValueError("dimensions should be the same size")
        for m in range(0, self.mlen):
            for n in range(0, self.nlen):
                self.userMatrix[m][n] = float(self.userMatrix[m][n]) + float(other.userMatrix[m][n])
        return Matrix(self.userMatrix)

    def __sub__(self, other):
        """ Subtracts two Matrix objects
       Parameters
       ----------
       other : Another Matrix object that has the same dimensions

       returns
       -------
       Matrix Object
           The subtraction of the two passed Matrix objects
       """
        if self.mlen != other.mlen or self.nlen != other.nlen:
            raise ValueError("dimensions should be the same size")
        for m in range(0, self.mlen):
            for n in range(0, self.nlen):
                self.userMatrix[m][n] = float(self.userMatrix[m][n]) + float(other.userMatrix[m][n])
        return Matrix(self.userMatrix)

    def __mul__(self, other):
        """ Element multiplication of two Matrix objects
       Parameters
       ----------
       other : Another Matrix object that has the same dimensions

       returns
       -------
       Matrix Object
           The element product of the two passed Matrix objects
       """
        if self.mlen != other.mlen or self.nlen != other.nlen:
            raise ValueError("dimensions should be the same size")
        for m in range(0, self.mlen):
            for n in range(0, self.nlen):
                self.userMatrix[m][n] = float(self.userMatrix[m][n]) + float(other.userMatrix[m][n])
        return Matrix(self.userMatrix)

    def __matmul__(self, other):
        """ Performs matrix multiplication on two Matrix objects
        
	Parameters
        ----------
        other : Another Matrix object that has the same inner dimensions

        returns
        -------
        Matrix Object
            The matrix product of the two passed Matrix objects
        """
        if self.nlen != other.mlen:
            raise ValueError("inner dimension should be the same size")
        temp_matrix = []
        for m in range(self.mlen):
            temp_rows = []
            for other_col in range(other.nlen):
                current = 0
                for n in range(self.nlen):
                    current += (self.userMatrix[m][n] * other.userMatrix[n][other_col])
                temp_rows.append(current)
            temp_matrix.append(temp_rows)
        return Matrix(temp_matrix)

    def trace(self):
        """ 
        Calculates the trace of the Matrix object. Requires a 1D Matrix Object

        Parameters:
	-----------
	
 	Takes no parameters

        returns
        -------
        int
            The calculated trace of the Matrix object
        """
        sum = 0
        if self.mlen != self.nlen:
            raise ValueError("matrix should be square")
        for x in range(self.mlen):
            sum += self.userMatrix[x][x]
        return sum

    def norm(self):
        """ 
        Calculates the norm of the Matrix object

        returns
        -------
        int
            The norm of the Matrix object
        """
        current = 0
        if self.mlen > 1 and self.nlen > 1:
            raise ValueError("matrix should be 1D")
        for m in range(self.mlen):
            for n in range(self.nlen):
                current += self.userMatrix[m][n] ** 2
        return math.sqrt(current)

    def reshape(self, new_m, new_n):
        """ 
        Reshapes the Matrix object the new dimensions passed

        Parameters
        ----------

        new_m : new m (height) of the matrix
        new_n : new n (width) of the matrix

        """
        if self.size != (new_m * new_n):
            raise ValueError("Matrix size should not change through reshaping")
        temp_matrix = []
        temp_row = []
        ii, jj = 0, 0
        while ii < self.mlen:
            while jj < self.nlen:
                if len(temp_row) < new_n:
                    temp_row.append(self.userMatrix[ii][jj])
                    jj += 1
                else:
                    temp_matrix.append(temp_row)
                    temp_row = []
            temp_matrix.append(temp_row)
            ii += 1
        self.mlen = new_m
        self.nlen = new_n
        self.userMatrix = temp_matrix


def main():
    # error_num = 0
    print("Checking Sizes")
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    print(A.shape)
    print(A.size)
    print(A)
    #
    # try:
    #     B = matrix.Matrix([[1, 2, 3], [4, 5]])
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # B = Matrix([[1, 1, 1], [1, 1, 1]])
    # print(B.shape)
    # print(B.size)
    # print(B)
    #
    # print("---- Add ----")
    # C = A + B
    # print(C)
    # A = Matrix([[1, 2, 3], [4, 5, 6]])
    # B = Matrix([[1, 1, 1], [1, 1, 1]])
    #
    # try:
    #     A = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    #     B = matrix.Matrix([[1, 1, 1]])
    #     C = A + B
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # print("---- Subtraction ----")
    # A = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    # B = matrix.Matrix([[1, 1, 1], [1, 1, 1]])
    # C = A - B
    # print(C)
    #
    # try:
    #     A = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    #     B = matrix.Matrix([[1, 1, 1]])
    #     C = A - B
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # print("---- Multi ----")
    # A = Matrix([[1, 2, 3]])
    # B = Matrix([[2, 2, 2]])
    #
    # X = A * B
    # print(X)
    #
    # X = A * B
    # print(X)
    #
    # try:
    #     A = matrix.Matrix([[1, 2, 3]])
    #     B = matrix.Matrix([[1, 2]])
    #     C = A * B
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # print("---- Matrix Multi ----")
    #
    # A = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # b = matrix.Matrix([[1], [2], [3]])
    # C = A @ b
    # print(C)
    # A = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    # b = matrix.Matrix([[10, 11], [20, 21], [30, 31]])
    # C = A @ b
    # print(C)
    #
    #
    # try:
    #     A = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    #     B = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    #     C = A @ B
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # print("---- Trace Test ----")
    # A = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(A.trace())
    #
    # try:
    #     A = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
    #     print(A.trace())
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    #
    # print("---- Vector Norm ----")
    # x = matrix.Matrix([[1, 2, 3]])
    # print(x.norm())
    #
    # x = matrix.Matrix([[1], [2], [3]])
    # print(x.norm())
    #
    # try:
    #     x = matrix.Matrix ([[1 ,2 ,3] ,[4 ,5 ,6]])
    #     print(x.norm())
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # print("---- Reshaping ----")
    # A = matrix.Matrix([[0, 1, 2, 3, 4, 5, 6, 7, 8]])
    # A.reshape(3, 3)
    # print(A)
    #
    # try:
    #     A = matrix.Matrix ([[0,1,2,3,4,5,6,7]])
    #     A.reshape(3, 3)
    #     print(A)
    # except ValueError as erro:
    #     print("Caught Error:", erro)
    #     error_num += 1
    #
    # if error_num == 8 :
    #     print("Passed all error tests!")

if __name__ == "__main__":
    main()
