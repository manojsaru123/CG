from classes.Point import Point
from classes.Line import Line
from classes.Ray import Ray
from classes.LineSegment import LineSegment

answer = input("What do you want to create ? (P or p for Point, L or l for Line, "
               "R or r for Ray, LS or ls for Line Segment): ")


def input_point(display_text):
    print(display_text)
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    point_input = Point(x, y)
    return point_input


if answer == "P" or "p":
    point = input_point("")
    print(point)

elif answer == "L" or "l":
    point1 = input_point("For First Point: ")
    point2 = input_point("For Second Point: ")
    line = Line(point1, point2)
    print(line)

elif answer == "R" or "r":
    point1 = input_point("Enter starting point for ray: ")
    point2 = input_point("Enter bounded point for ray: ")
    ray = Ray(point1, point2)
    print(ray)

elif answer == "LS" or "ls":
    point1 = input_point("Enter starting point for line segment: ")
    point2 = input_point("Enter ending point for line segment: ")
    line_segment = LineSegment(point1, point2)
    print(line_segment)

else:
    print("Please select the option from above.")