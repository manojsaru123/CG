from classes.Point import Point


class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.startPoint = float("-inf")
        self.firstPoint = point_a
        self.secondPoint = point_b
        self.endPoint = float("inf")

    def __str__(self):
        return "Line with two coordinate ({0},{1}) and ({2}, {3})".format(self.firstPoint.x, self.firstPoint.y, self.secondPoint.x, self.secondPoint.y)