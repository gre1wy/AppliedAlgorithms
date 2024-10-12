class BitVectorSet:
    def __init__(self, t):
        """Ініціалізує множину з t 64-бітних регістрів (універсум з 64t елементів)."""
        self.t = t 
        self.vector = [0] * t

    def _get_index(self, element):
        """Повертає індекс регістра та позицію біта в цьому регстрі"""
        register_index = element >> 6 # Індекс 64-бітного регістра math.log2(64)
        bit_position = element & (64-1) # Позиція біта в регістрі
        return register_index, bit_position
    
    def have(self, element):
        """Перевіряє чи існує елемент в множині"""
        reg_index, b_position = self._get_index(element)
        return self.vector[reg_index] & (1 << b_position) != 0
        
    def add(self, element):
        """Додає елемент в множину"""
        reg_index, b_position = self._get_index(element)
        self.vector[reg_index] |= 1 << b_position

    def delete(self, element):
        """Видаляє елемент з множини"""
        reg_index, b_position = self._get_index(element)
        self.vector[reg_index] &= ~(1 << b_position)

    def union(self, other):
        """Повертає обєднання двух множин"""
        if self.t != other.t:
            raise ValueError("Множини мають різні розміри")
        result = BitVectorSet(self.t)
        result.vector = [self.vector[i] | other.vector[i] for i in range(self.t)]
        return result
    
    def intersection(self, other):
        """Повертає перетин двух множин"""
        if self.t != other.t:
            raise ValueError("Множини мають різні розміри")
        result = BitVectorSet(self.t)
        result.vector = [self.vector[i] & other.vector[i] for i in range(self.t)]
        return result
    
    def diff(self, other):
        """Повертає різницю двух множин"""
        result = BitVectorSet(self.t)
        result.vector = [self.vector[i] & ~other.vector[i] for i in range(self.t)]
        return result
    
    def sym_diff(self, other):
        """Повертає симетричну різницю: елементи, які є в одному з множин, але не в обох."""
        if self.t != other.t:
            raise ValueError("Множини мають різні розміри")
        result = BitVectorSet(self.t)
        result.vector = [self.vector[i] ^ other.vector[i] for i in range(self.t)]
        return result
    
    def issubset(self, other):
        """Перевіряє, чи є поточна множина підмножиною іншої."""
        if self.t != other.t:
            raise ValueError("Множини мають різні розміри")
        # Для кожного регістра перевіряємо, чи всі встановлені біти self є в other
        for i in range(self.t):
            if self.vector[i] & ~other.vector[i] != 0: 
                return False
        return True
    
    def clear(self):
        """Очищає множину, встановлюючи всі біти в 0."""
        self.vector = [0] * self.t
    
    def __str__(self):
        """Повертає бітовий вектор як рядок для зручного перегляду."""
        return ''.join(f'{reg:064b}' for reg in reversed(self.vector))