from classes.Point import Point


class LineSegment:
    def __init__(self, start_point: Point, end_point: Point):
        self.startPoint = start_point
        self.endPoint = end_point

    def slope(self):
        y2 = self.endPoint.y
        y1 = self.startPoint.y
        x2 = self.endPoint.x
        x1 = self.startPoint.x

        return (y2-y1) / (x2 - x1)

    def __str__(self):
        return "Line segment with starting point ({0},{1}) and end point ({2},{3})".format(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y)