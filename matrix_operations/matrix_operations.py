import numpy as np
class Matrix:
    """ Matrix class for calculating 
    the matrix operations.
    
    Attributes:
        out (array) representing matrix
        determinant (float) representing the determinant value of the matrix
        element (float) representing an element at a given position
        dimensions (tuple) representing the dimensions of a matrix
    """
    def __init__(self,out=0, determinant=0, element=0, dimensions=0):
        self.out = out
        self.determinant = determinant
        self.element = element
        self.dimensions = dimensions
    def add(self,mat1,mat2):
        """Method to calculate the addition of two matrices or
            a matrix and a scalar.
        Args:
            array: matrix 1
            array: matrix 2

        Returns:
            array: addition of two matrices
        """
        if(np.shape(mat1)==np.shape(mat2)):
            result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        elif(isinstance(mat2,int)==True):
            result = [[mat1[i][j] + mat2 for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        else:
            print('wrong format')
    def sub(self,mat1,mat2):
        """Method to calculate the subtraction of two matrices or
            a matrix and a scalar.
        Args:
            array: matrix 1
            array: matrix 2

        Returns:
            array: addition of two matrices
        """
        if(np.shape(mat1)==np.shape(mat2)):
            result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        elif(isinstance(mat2,int)==True):
            result = [[mat1[i][j] - mat2 for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        else:
            print('wrong format')
    def mul(self,mat1,mat2):
        """Method to calculate the multiplication of two matrices or
            a matrix and a scalar.
        Args:
            array: matrix 1
            array: matrix 2

        Returns:
            array: multiplication of two matrices
        """
        if(isinstance(mat2,int)==True):
            result = [[mat1[i][j] * mat2 for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        elif(len(mat1[0])==len(mat2)):
            result = [[sum(a*b for a,b in zip(i,j)) for j in zip(*mat2)] for i in mat1]
            self.out = result
            return self.out
    def div(self,mat1,mat2):
        """Method to calculate the division of two matrices or
            a matrix and a scalar.
        Args:
            array: matrix 1
            array: matrix 2

        Returns:
            array: division of two matrices
        """
        if(np.shape(mat1)==np.shape(mat2)):
            result = [[mat1[i][j] / mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        elif(isinstance(mat2,int)==True):
            result = [[mat1[i][j] / mat2 for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        else:
            print('wrong format')
    def transpose(self,mat):
        """Method to calculate the transpose of a matrix
        Args:
            array: matrix 1
        Returns:
            array: transpose of the matrix
        """
        result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        self.out = result
        return self.out
    def inverse(self,mat):
        """Method to calculate the inverse of a matrix
        Args:
            array: matrix 1
        Returns:
            array: inverse of the matrix
        """
        result = np.linalg.inv(mat)
        self.out = result
        return self.out
    def det(self,mat):
        """Method to calculate the determinant of a matrix
        Args:
            array: matrix 1
        Returns:
            array: determinant of the matrix
        """
        result = np.linalg.det(mat)
        self.determinant = result
        return self.determinant
    def get_element(self,mat,row,column):
        """Method to get an element of a matrix
        Args:
            array: matrix 1
        Returns:
            float: required element in the matrix
        """
        result = mat[row-1][column-1]
        self.element = result
        return self.element 
    def dim(self,mat):
        """Method to calculate the dimensions of a matrix
        Args:
            array: matrix 1
        Returns:
            tuple: dimensions of the matrix
        """
        result = np.shape(mat)
        self.dimensions = result
        return self.dimensions         

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]  
Z = 5  
m = Matrix()
print(m.det(X))



        

