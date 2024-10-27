class Vector:
    def __init__(self, elements):
        """
        Initializes a vector with the given elements.

        :param elements: A list of elements of the vector
        :type elements: list
        """

        self.elements = elements
    
    def __add__(self, other):
        """
        Returns the sum of two vectors.

        :param other: The other vector to be summed
        :type other: Vector
        :return: The sum of the two vectors
        :rtype: Vector
        """
        self.size_error(other)
        return Vector([a + b for a, b in zip(self.elements, other.elements)])
    
    def __sub__(self, other):
        """
        Returns the difference of two vectors.

        :param other: The other vector to be subtracted
        :type other: Vector
        :return: The difference of the two vectors
        :rtype: Vector
        """
        self.size_error(other)
        return Vector([a - b for a, b in zip(self.elements, other.elements)])
    
    def __mul__(self, other):
        """
        Returns multiplication of the vector with a scalar or another vector.

        If the other operand is a scalar (int or float), the vector is multiplied element-wise.

        If the other operand is a vector, the scalar multiplication (dot product) of the two vectors is returned.

        :param other: The other operand to be multiplied
        :type other: int or float or Vector
        :return: The result of the scalar multiplication
        :rtype: Vector or int
        """
        # Scalar multiplication
        if isinstance(other, (int, float)):  
            return Vector([a * other for a in self.elements])
        # Scalar multiplication of vectors
        elif isinstance(other, Vector):  
            self.size_error(other)
            return sum(a * b for a, b in zip(self.elements, other.elements)) 
        else:
            raise TypeError("Unsupported operand type for *: 'Vector' and '{}'".format(type(other).__name__))
    def dot(self, other):
        return Vector([a * b for a, b in zip(self.elements, other.elements)])
        
    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value
    
    def __repr__(self):
        return f"Vector({self.elements})"
    
    def size_error(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        
    def __len__(self):
        return len(self.elements)