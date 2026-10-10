class Rectangle:
    def __init__ (self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width: .2f}cm"

    @property 
    def height(self):
        return f"{self._height: .2f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print("ERROR: Width must be GREATER than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height

        else:
            print("ERROR: Height must be GREATER than 0")

    @height.deleter
    def height(self):
        del self._height
        print("Width got deleted.. :(")

    @width.deleter
    def width(self):
        del self._width
        print("Height got deleted.. :(")

# --Testing area--

#Test 1: Making the rectangles
rectangle1 = Rectangle(12.4, 13.5)
rectangle2 = Rectangle(8, 7)

#Test 2: Updating values (setters)
rectangle1.width = 15.5
rectangle2.height = 16
 
#Test 3: Printing the values 
print(f"Rectangle 1 - Width: {rectangle1.width}, Height: {rectangle1.height}")
print(f"Rectangle 2 - Width: {rectangle2.width}, Height: {rectangle2.height}")

#Test 4: Testing the negative values
rectangle1.width = -5

#Test 5: Testing deleters
del rectangle1.width
del rectangle1.height



