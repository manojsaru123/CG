class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "Point with x coordinate {0} and y coordinate {1}".format(self.x, self.y)

