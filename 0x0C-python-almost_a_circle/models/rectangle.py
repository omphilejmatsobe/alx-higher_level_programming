#!/usr/bin/python3


"""
===========================
Module of Rectangle
===========================
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle of Rectangle and inherits
    from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init constructor
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private width function"""

        return self.__width__

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width__ = value

    @property
    def height(self):
        """private height function"""

        return self.__height__

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height__ = value

    @property
    def x(self):
        """private x function"""

        return self.__x__

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x__ = value

    @property
    def y(self):
        """private y function"""

        return self.__y__

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y__ = value

    def area(self):
        """
        area method for rectangle area
        """

        return self.width * self.height

    def display(self):
        """
        display function, to print a rectangle
        """

        r = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(r, end='')

    def __str__(self):
        """
        Returns string info about this rectangle
        """

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args):
        """
        Assigns each argument to an attribute
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
