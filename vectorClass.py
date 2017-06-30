class SizeMismatch(Exception):

    pass



class IllegalSize(Exception):

    pass



class IllegalIndex(Exception):

    pass



class Vector:

    "Class to manage vectors (unidimensional arrays) of floating-point numbers"



    def __init__(self, size):

        """Constructor of vector. If size <= 0 IllegalSize ir raised

        Initialy the vector has all elements as zero"""

        try:

            if size < 1:

                raise IllegalSize

            else:

                self.size = size

                self.vector = [0 for i in range(self.size)]

                

        except IllegalSize:

            print("Size must be greater or equal to 1")

        

    def getSize(self):

        "Method that returns the size of the vector"

        return self.size



    def get(self, i):

        """Method that returns the element of a vector at position i

        If i>=self.size or i<0, IllegalIndex is called"""

        try:

            if i < 0 or i >= self.size :

                raise IllegalIndex

            else:

                return self.vector[i]

        except IllegalIndex:

            print("Index out of range")



    def set(self, i, value):

        """Method that mutates the element of a vector at position i

        with that of value. If i>=self.size or i<0,

        IllegalIndex is called"""

        try:

            if i < 0 or i >= self.size :

                raise IllegalIndex

            else:

                self.vector[i] = value

        except IllegalIndex:

            print("Index out of range")



    def __add__(self, other):

        """Overloading the  + operator to compute the sum of the 2 vectors

        (self+other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

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

        """Overloading the  - operator to compute the substraction of the 2 vectors

        (self-other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

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

        """Overloading the  * operator to compute the dot-product of the 2 vectors

        (self*other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

        if type(other) == float:

            v = Vector(self.size)

            for i in range(self.size):

                v.set(i, self.get(i)*other)

            return v

        else:

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

        """Overloading the  == operator to compare 2 vectors (self==other).

        If the vectors have different sizes, SizeMismatch exception is raised"""

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

        """Overloading the  != operator to compare 2 vectors (self!=other).

        If the vectors have different sizes, SizeMismatch exception is raised"""

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

        "Overloading operator + to return a copy of the vector (+self)"

        v = Vector(self.size)

        for i in range(self.size):

             v.set(i, self.get(i))

        return v



    def __neg__(self):

        """Overloading the - operator to return a copy of the vector

        where the signs of the elements are changed (-self)."""

        v = Vector(self.size)

        for i in range(self.size):

             v.set(i, -1 * self.get(i))

        return v



    def __repr__(self):

        "Canonical string representation of the object"

        return 'Vector({}, {})'.format(self.size, tuple(self.vector))



    def __str__(self):

        string = "<"

        for i in range(self.size):

            if i == self.size-1:

                string +='{}> '.format(self.get(i))

            else:

                string +='{}, '.format(self.get(i))

        return string



    def __iadd__(self, other):

        """Overloading the  += operator to compute the substraction of the 2 vectors and

        storing it in self (self+=other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

        try:

            if self.size != other.size:

                raise SizeMismatch

            else:

                for i in range(self.size):

                    self.set(i, self.get(i) + other.get(i))

                return self

        except SizeMismatch:

            print("Vectors have different sizes")



    def __isub__(self, other):

        """Overloading the  -= operator to compute the substraction of the 2 vectors and

        storing it in self (self-=other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

        try:

            if self.size != other.size:

                raise SizeMismatch

            else:

                for i in range(self.size):

                    self.set(i, self.get(i) - other.get(i))

                return self

        except SizeMismatch:

            print("Vectors have different sizes")



    def __imul__(self, other):

        """Overloading the  *= operator to compute the scalar multiplication of a vector and

        storing it in self (self-=other). If the vectors have different sizes, SizeMismatch

        exception is raised"""

        if type(other) == float:

            for i in range(self.size):

                self.set(i, self.get(i) * other )

            return self
            
        elif type(other) == Vector:
          
          for i in range(self.size):
            
            self.set(i, self.get(i) * other.get(i) )
        
          return self

        else:

            print("In-place multiplication must be between vector and a float")



    def __getitem__(self, i):

        "Method that calls self.get(i) using the [] operator"

        return self.get(i)



    def __setitem__(self, i, value):

        "Method that calls self.set(i, value) using the [] operator"

        self.set(i, value)

    

    def min(self):

        "Method that returns the minimum of the vector"

        """

        minimum = self.get(0)

        for i in range(1,self.size):

            if minimum > self.get(i):

                minimum = self.get(i)

        return minimum

        """

        return min(self.vector)

    

    def max(self):

        "Method that returns the maximum of the vector"

        """

        maximum = self.get(0)

        for i in range(1,self.size):

            if maximum < self.get(i):

                maximum = self.get(i)

        return maximum

                """

        return max(self.vector)

    

    def sum(self):

        "Method that returns the sum of the elements of the vector"

        total = 0

        for i in range(self.size):

            total += self.get(i)

        return total

    

    def average(self):

        "Method that returns the average of the elements of the vector"

        return self.sum() / self.getSize()


a = Vector(5)

print("Vector size:", a.getSize() )

a.set(0,1)
a.set(1,2)
a.set(2,3)
a.set(3,4)
a.set(4,5)

print("Vector A:", a)

print("Position 2 value:", a.get(2) )

print("Minimum value:", a.min() )

print("Maximum value:", a.max() )

print("Sum of all values:", a.sum() )

print("Average:", a.average() )

print("")

b = Vector(5)

b.set(0,-3)
b.set(1,-4)
b.set(2,-5)
b.set(3,-6)
b.set(4,-7)

print("Vector B:", b)

print("A + B:", a + b)

print("A - B:", a - b)

print("A * B:", a * b)

print("A == B", a == b)

print("A != B:", a != b)

print("Positive of B:", +b)

print("Negative of A:", -a)

print("")

c = Vector(5)

print(c)

c += b

print("After C += B:", c)

c -= a

print("After C -= A:", c)

c *= b

print("After C *= B:", c)

c[0] = 2
c[1] = 10
c[2] = 5
c[3] = -11
c[4] = 8

print("Position c[3]:", c[3] )
print("Position c[4]:", c[4] )
