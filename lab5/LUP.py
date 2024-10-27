from SquaredMatrix import SquaredMatrix
from Vector import Vector
import copy
class LinearSystem:
    def __init__(self, A, b):
        """
        Initialize the linear system with matrix A and vector b.
        A: List of lists representing the matrix
        b: List representing the right-hand side vector
        """
        self.A = SquaredMatrix(copy.deepcopy(A)) 
        self.b = Vector(copy.deepcopy(b))

    def lup_decomposition(self):
        """
        Perform LUP decomposition of matrix A.
        Returns: (A, P) where A is modified to contain L and U matrices, and P is the permutation vector.
        """
        n = len(self.A)
        P = [i for i in range(n)]
        
        for k in range(n):
            
            # Find the pivot element
            pivot = k
            for i in range(k, n):
                if abs(self.A[i][k]) > abs(self.A[pivot][k]):
                    pivot = i

            if self.A[pivot][k] == 0:
                raise ValueError("Matrix is singular and cannot be decomposed.")
            
            # Swap rows in both A and P
            self.A[k], self.A[pivot] = self.A[pivot], self.A[k]
            P[k], P[pivot] = P[pivot], P[k]
            
            # Decompose into L and U
            for i in range(k+1, n):
                self.A[i][k] /= self.A[k][k]
                for j in range(k+1, n):
                    self.A[i][j] -= self.A[i][k] * self.A[k][j]
        
        return self.A, P

    def lup_solve(self, A, P, b):
        """
        Solve the system of equations given LUP decomposition and right-hand side vector b.
        A: Matrix after LUP decomposition
        P: Permutation vector
        b: Right-hand side vector
        Returns: Solution vector x
        """
        n = len(A)
        x = [0] * n
        y = [0] * n
        b_P = [b[P[i]] for i in range(n)]  

        for i in range(n):
            y[i] = b_P[i] - sum(A[i][j] * y[j] for j in range(i))
        
        for i in range(n-1, -1, -1):
            x[i] = (y[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
        
        return x

    def solve(self):
        """
        Solve the linear system using LUP decomposition.
        Returns: Solution vector x
        """
        A, P = self.lup_decomposition()
        return self.lup_solve(A, P, self.b)