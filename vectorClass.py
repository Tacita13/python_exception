class SizeMismatch(Exception):
    pass

class IllegalSize(Exception):
    pass

class IllegalIndex(Exception):
    pass

class Vector:
    "Class to manage vectors (unidimensional arrays) of floating-point numbers"

    def __init__(self, size):
        try:
            if size < 1:
                raise IllegalSize
            else:
                self.size = size
                self.vector = [0 for i in range(self.size)]
                
        except IllegalSize:
            print("Size must be greater or equal to 1")
        
    def getSize(self):
        return self.size

    def get(self, i):
        try:
            if i < 0 or i >= self.size :
                raise IllegalIndex
            else:
                return self.vector[i]
        except IllegalIndex:
            print("Index out of range")

    def set(self, i, value):
        try:
            if i < 0 or i >= self.size :
                raise IllegalIndex
            else:
                self.vector[i] = value
        except IllegalIndex:
            print("Index out of range")

    def __add__(self, other):
        try:
            if self.size != other.size:
                raise SizeMismatch
            else:
                v = Vector(self.size)
                for i in range(self.size):
                    v.set(i, self.get(i) + other.get(i))
            return v
        except SizeMismatch:
            print("Vectors have different sizes")
            
    def __sub__(self, other):
        try:
            if self.size != other.size:
                raise SizeMismatch
            else:
                v = Vector(self.size)
                for i in range(self.size):
                    v.set(i, self.get(i) - other.get(i))
            return v
        except SizeMismatch:
            print("Vectors have different sizes")

    def __mul__(self, other):
        try:
            if self.size != other.size:
                raise SizeMismatch
            else:
                dotProduct = 0
                for i in range(self.size):
                   dotProduct += self.get(i) * other.get(i)
            return dotProduct
        except SizeMismatch:
            print("Vectors have different sizes")

    def __eq__(self, other):
        try:
            if self.size != other.size:
                raise SizeMismatch
            else:
                for i in range(self.size):
                   if self.get(i) != other.get(i):
                       return False
                   else:
                        return True
        except SizeMismatch:
            print("Vectors have different sizes")

    def __ne__(self, other):
        try:
            if self.size != other.size:
                raise SizeMismatch
            else:
                equals = 0
                for i in range(self.size):
                   if self.get(i) == other.get(i):
                       equals += 1
                if equals == self.size:
                    return False
                else:
                    return True
        except SizeMismatch:
            print("Vectors have different sizes")

    def __pos__(self):
        v = Vector(self.size)
        for i in range(self.size):
             v.set(i, self.get(i))
        return v

    def __neg__(self):
        v = Vector(self.size)
        for i in range(self.size):
             v.set(i, -1 * self.get(i))
        return v

    def min(self):
        """
        minimum = self.get(0)
        for i in range(1,self.size):
            if minimum > self.get(i):
                minimum = self.get(i)
        return minimum
        """
        return min(self.vector)
    
    def max(self):
        """
        maximum = self.get(0)
        for i in range(1,self.size):
            if maximum < self.get(i):
                maximum = self.get(i)
        return maximum
                """
        return max(self.vector)
    
    def sum(self):
        total = 0
        for i in range(self.size):
            total += self.get(i)
        return total
    
    def average(self):
        return self.sum()/self.getSize()
