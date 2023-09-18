#!/usr/bin/python3


"""
===========================
module with square class
===========================
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        the __init__ contructor for the class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns info about this square
        """

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size function
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update functionto assign a list of attributes
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for u, v in kwargs.items():
                if u == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif u == "size":
                    self.size = v
                elif u == "x":
                    self.x = v
                elif u == "y":
                    self.y = v

    def to_dictionary(self):
        """
         returns the dictionary representation of a Rectangle
        """

        return {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y
        }
