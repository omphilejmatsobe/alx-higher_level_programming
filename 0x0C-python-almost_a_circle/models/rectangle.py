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

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private width function"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """private height function"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """private x function"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """private y function"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

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

    def update(self, *args, **kwargs):
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

        elif kwargs and len(kwargs) != 0:
            for u, z in kwargs.items():
                if u == "id":
                    if z is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = z
                elif u == "width":
                    self.width = z
                elif u == "height":
                    self.height = z
                elif u == "x":
                    self.x = z
                elif u == "y":
                    self.y = z

    def to_dictionary(self):
        '''Returns dictionary representation rectangle'''

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
