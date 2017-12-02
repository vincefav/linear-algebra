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

def dot_product(vector_one, vector_two):
    new_vector = []
    for i in range(len(vector_one)):
        new_vector.append(vector_one[i] * vector_two[i])
    return sum(new_vector)
    
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
        return (self.g[0][0]*self.g[1][1]) - (self.g[0][1]*self.g[1][0])
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        t = 0
        # TODO - your code here
        for i in range(self.h):
            t += self[i][i]
        return t

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

        if self.w == 1 and self.h == 1:
            inverse = [[1/self.g[0][0]]]
        elif self.w == 2 and self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            scalar = 1 / ( (a*d) - (b*c) )
            inverse = [ [ d, -b ], [ -c, a ] ]

            for i in range(self.h):
                for j in range(self.w):
                    inverse[i][j] *= scalar
        
        return Matrix(inverse)
                    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transposition = zeroes(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                transposition[j][i] = self.g[i][j]
        
        return Matrix(transposition)
        
        
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
    
    def __len__(self):
        return self.h
    
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        sum_ = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                sum_[i][j] = self.g[i][j] + other.g[i][j]
                
        return Matrix(sum_)

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
        neg = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                neg[i][j] = self.g[i][j] * -1
                
        return Matrix(neg)
    
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        difference = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                difference[i][j] = self.g[i][j] - other.g[i][j]
                
        return Matrix(difference)    
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        m_rows = self.h
        p_columns = other.w
        product = []
        other_T = other.T()
        
        for i in range(self.h):
            row = []
            for j in range(other_T.h):
                row.append(dot_product(self[i], other_T[j]))
            product.append(row)
        return Matrix(product)
      
        
        

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
            scaled = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    scaled[i][j] = self.g[i][j] * other

            return Matrix(scaled)