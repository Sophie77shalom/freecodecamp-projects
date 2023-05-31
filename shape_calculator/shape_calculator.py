class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def __str__(self):
        return f"Square(side={self.width})"

## Example
# Create a Rectangle object
rectangle = Rectangle(5, 10)

# Print the properties of the Rectangle object
print(rectangle.get_area())       
print(rectangle.get_perimeter())  
print(rectangle.get_diagonal())   
print(rectangle.get_picture())    
                            
                                 
                                 
                                 
print(rectangle.get_amount_inside(Square(2)))  
print(rectangle)  

# Create a Square object
square = Square(4)

# Print the properties of the Square object
print(square.get_area())      
print(square.get_perimeter())  
print(square.get_diagonal())   
print(square.get_picture())    
                               
                               
                               
print(square.get_amount_inside(Rectangle(2, 2)))  
print(square)  

# Modify the Square object using set_side method
square.set_side(6)
print(square.get_area())       
print(square.get_perimeter())  
print(square.get_picture())    
                               
                               
                               
                               
print(square)  
