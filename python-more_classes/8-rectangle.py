#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Define a Rectangle with withd and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return to the rectangle area
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Return to rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """
        Prints rectangle using #
        or o if empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = ("{}".format(self.print_symbol)) * self.width
        rectangle = width
        for i in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
        """
        Returns a string representation
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        Prints a message when rectangle deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectngle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
