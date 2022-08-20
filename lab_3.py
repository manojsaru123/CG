from classes.Point import Point
from classes.Line import Line
import matplotlib.pyplot as plt


def check_intersection(first_line_points, second_line_points):
    line_1 = Line(first_line_points[0], first_line_points[1])
    line_2 = Line(second_line_points[0], second_line_points[1])

    abc_turntest = line_1.check_turn_test(line_2.point_a)
    abd_turntest = line_1.check_turn_test(line_2.point_b)

    if abc_turntest == abd_turntest:
        print("These two lines doesn't intersect")
    elif abc_turntest != "colinear" and abd_turntest != "colinear":
        print("These two lines intersect and is a proper intersection")
    else:
        point_to_check_betweenness = line_2.point_a if abc_turntest == "colinear" else line_2.point_b
        is_between = line_1.check_betweenness(point_to_check_betweenness)
        if is_between:
            print("Improper Intersection")
        else:
            print("No Intersection, just collinear")

# Proper INtersection
first_line_points = [Point(5, 10), Point(2, 2)]
second_line_points = [Point(3, 1), Point(3, 8)]
line_1 = Line(first_line_points[0], first_line_points[1])
line_2 = Line(second_line_points[0], second_line_points[1])

line_1.check_intersection(line_2)

plt.plot([line_1.point_a.x, line_1.point_b.x], [line_1.point_a.y, line_1.point_b.y])
plt.plot([line_2.point_a.x, line_2.point_b.x], [line_2.point_a.y, line_2.point_b.y])
plt.show()


# Improper Intersection

first_line_points = [Point(5, 10), Point(2, 2)]
second_line_points = [Point(2, 2), Point(2, 8)]

line_1 = Line(first_line_points[0], first_line_points[1])
line_2 = Line(second_line_points[0], second_line_points[1])

line_1.check_intersection(line_2)

plt.plot([line_1.point_a.x, line_1.point_b.x], [line_1.point_a.y, line_1.point_b.y])
plt.plot([line_2.point_a.x, line_2.point_b.x], [line_2.point_a.y, line_2.point_b.y])
plt.show()


# No Intersection
first_line_points = [Point(5, 10), Point(2, 2)]
second_line_points = [Point(1, 1), Point(1, 8)]

line_1 = Line(first_line_points[0], first_line_points[1])
line_2 = Line(second_line_points[0], second_line_points[1])

line_1.check_intersection(line_2)

plt.plot([line_1.point_a.x, line_1.point_b.x], [line_1.point_a.y, line_1.point_b.y])
plt.plot([line_2.point_a.x, line_2.point_b.x], [line_2.point_a.y, line_2.point_b.y])
plt.show()
