from classes.Polygon import Polygon
from classes.Point import Point
import matplotlib.pyplot as plt

points = [Point(1,1), Point(4,1), Point(4,4), Point(1,4)]
polygon = Polygon(points)
polygon.draw()
plt.show()

print("convex polygon" if polygon.is_convex() else "reflex polygon")
