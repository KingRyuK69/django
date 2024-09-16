# Task: Rectangle Class with Iteration Capability

# Code:
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Use a generator to return length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Usage example
rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)

# Output:
# {'length': 10}
# {'width': 5}

# Explanation:
# The Rectangle class implements the __iter__ method to enable iteration over its dimensions. The __iter__ method returns a generator that yields dictionaries containing the length and width of the rectangle. When the Rectangle instance is iterated over in a for loop, the dimensions are printed in the required format.