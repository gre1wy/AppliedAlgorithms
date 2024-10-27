from Vector import Vector
class SquaredMatrix:
    def __init__(self, rows):
        
        row_len = len(rows[0]) # number of columns
        num_rows = len(rows) # numer of rows

        if row_len!=num_rows:
            raise ValueError("Matrix should be squared.")
        if not all(len(row) == row_len for row in rows):
            raise ValueError("All rows (vectors) must have the same length.")
        
        self.rows = [Vector(row) for row in rows]
        self.size = row_len

    def diff_size(self, other):
        if self.size != other.size:
            raise ValueError("Matrices must be of the same size.")
    
    def __add__(self, other):
        self.diff_size(other)
        added_rows = [self.rows[i] + other.rows[i] for i in range(self.size)]
        return SquaredMatrix(added_rows)
    
    def __sub__(self, other):
        self.diff_size(other)
        
        subtracted_rows = [self.rows[i] - other.rows[i] for i in range(self.size)]
        return SquaredMatrix(subtracted_rows)
    
    def __mul__(self, other):
        # Scalar multiplication
        if isinstance(other, (int, float)): 
            scaled_rows = [row * other for row in self.rows]
            return SquaredMatrix(scaled_rows)
        
        # Multiplication of matrix and vector
        elif isinstance(other, Vector):  
            if self.size != len(other):
                raise ValueError("Matrix columns must equal vector size.")
            
            result_elements = [row * other for row in self.rows]
            return Vector(result_elements)
        
        # Multiplication of two matrices
        elif isinstance(other, SquaredMatrix):  
            if self.size != other.size:
                raise ValueError("Matrix A's number of columns must equal matrix B's number of rows.")
            
            result_rows = []
            for i in range(self.size):
                new_row = []
                for j in range(other.size):
                    new_row.append(sum(self.rows[i][k] * other.rows[k][j] for k in range(self.size)))
                result_rows.append(Vector(new_row))
            
            return SquaredMatrix(result_rows)
        else:
            raise TypeError(f"Unsupported operand type for *: 'Matrix' and '{type(other).__name__}'")
        
    def __setitem__(self, index, new_row):
        if not isinstance(new_row, Vector):
            try:
                new_row = Vector(new_row)
            except:
                raise TypeError("New row must be an instance of the Vector class.")
        if len(new_row) != self.size:
            raise ValueError("New row must have the same number of elements as other rows.")
        
        self.rows[index] = new_row
        
    def __getitem__(self, index):
        
        return self.rows[index].elements
        
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"Matrix({[row.elements for row in self.rows]})"