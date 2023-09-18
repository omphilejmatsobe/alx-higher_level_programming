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
        """size function"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value
