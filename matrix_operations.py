import numpy as np
class Matrix:
    def __init__(self,out=0):
        self.out = out
    def add(self,mat1,mat2):
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
        if(isinstance(mat2,int)==True):
            result = [[mat1[i][j] * mat2 for j in range(len(mat1[0]))] for i in range(len(mat1))]
            self.out = result
            return self.out
        elif(len(mat1[0])==len(mat2)):
            result = [[sum(a*b for a,b in zip(i,j)) for j in zip(*mat2)] for i in mat1]
            self.out = result
            return self.out
    def div(self,mat1,mat2):
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
        result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        self.out = result
        return self.out
    def inverse(self,mat):
        result = np.linalg.inv(mat)
        self.out = result
        return self.out
    def det(self,mat):
        result = np.linalg.det(mat)
        self.out = result
        return self.out
    def get_element(self,mat,row,column):
        row -= 1
        column -= 1 
        result = mat[row][column]
        self.out = result
        return self.out 
    def dim(self,mat):
        result = np.shape(mat)
        self.out = result
        return self.out         

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]  
Z = 5  
m = Matrix()
print(m.dim(X))



        

