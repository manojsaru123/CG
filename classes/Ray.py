from classes.Point import Point

class Ray:
    def __init__(self, start_point: Point, mid_point: Point):
        self.startPoint = start_point
        self.midPoint = mid_point
        self.endPoint = float("inf")

    def __str__(self):
        return "Ray with starting point ({0}, {1}) and mid point ({2}, {3})".format(self.startPoint.x, self.startPoint.y, self.midPoint.x, self.midPoint.y)

