import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if(self.h == 1):
            d = self[0][0]
        elif(self.h == 2):
            ad = (self[0][0]) * (self[1][1])
            bc = (self[0][1]) * (self[1][0])
            d = ad - bc
        
        return d

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        s = 0
        for i in range(self.h):
            for j in range(self.w):
                if(i == j):
                    s += (self[i][j])
        
        return s

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        
        if(self.h == 1):
            
            inverse =[[1/self.determinant()]]
            #inverse.append(1/self[0][0])
 
        
        elif(self.h == 2):
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            
            inverse = [[d, -b],[-c, a]]
            
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = (1/self.determinant()) * inverse[i][j]
                    
                    
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        matrix_transpose = []
        
        for i in range(self.w):
            matrix_transpose_row = []
            
            for j in range(self.h):
                matrix_transpose_row.append(self[j][i])
            
            matrix_transpose.append(matrix_transpose_row)
        
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j]+other[i][j])
            
            matrixSum.append(row)
        
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg = []
        for i in range(self.h):
            neg_row = []
            for j in range(self.w):
                neg_row.append(- self[i][j])
            
            neg.append(neg_row)
        
        
        
        return Matrix(neg)
                
                
               
        return self

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixDifference = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j]-other[i][j])
            
            matrixDifference.append(row)
            
        
        return Matrix(matrixDifference)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #

        rows = self.h
        columns = other.w
    
        
        result = []


        for r in range(rows):
            row_result = []
            row = self[r]
        
            for c in range(columns):
                column = []
                for r in range(other.h):
                    column.append(other[r][c])
                    
                dot_product = 0
    
                for i in range(len(row)):
                    dot_product += (row[i] * column[i])

           
                row_result.append(dot_product)
    

            result.append(row_result)

        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] *= other   
        
        
        
        return self
            
            
            
            
            
            
            
            