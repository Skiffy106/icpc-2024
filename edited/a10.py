n = int(input())

from math import *

def slope1(coords):
    slopes = []
    for i, cord1 in enumerate(coords):
        for j, cord2 in enumerate(coords[i+1:]):
            x1, y1 = cord1
            x2, y2 = cord2
            if x2 == x1:
                slopes.append(10 ** 5)
                continue
            slope = float(y2 - y1) / float(x2 - x1)
            slopes.append(slope)

    for i in range(len(slopes)):
        matches = 0
        for j in range(i+1, len(slopes)):
            if slopes[i] == slopes[j]:
                matches += 1
        if matches > 1:
            return False
    return True

def vec_diff(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return x2-x1, y2-y1

def vec_norm(x1, y1, x2, y2):
    y, x = vec_diff((x1, y1), (x2, y2))
    return -x, y # (-x, y), (x, -y)

def slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x2 == x1:
        return 10 ** 6
    return (y2-y1)/(x2-x1)

def line_eq(line):
    p1, p2 = line
    m1 = slope(p1, p2)
    b1 = p1[1] - m1 * p1[0]  # b = y - mx
    return m1, b1

def triangle(coords):
    for outer_idx in range(len(coords)):

        point = coords[outer_idx]
        tri: list = coords.copy()
        tri.remove(point)
        print(point)

        # print(tri)

        lines = []
        line_eqs = []
        for i in range(len(tri)):
            for j in range(i+1, len(tri)):
                lines.append((tri[i], tri[j]))
                line_eqs.append(line_eq((tri[i], tri[j])))

        def intersection(line1, line2):
            m1, b1 = line_eq(line1)
            m2, b2 = line_eq(line2)

            x = (b1 - b2)/(m2 - m1)
            y = m1*x + b1

            return x, y

        for i in range(len(lines)):
            print(lines)
            base_line = lines[i]
            point1, point2 = base_line
            x1, y1 = point1
            x2, y2 = point2
            norm = vec_norm(x1, y1, x2, y2)
            normLine = (point, norm)
            normLine_eq = line_eq(normLine)

            intersections = []
            for j in range(len(lines)):
                test_line = lines[j]
                tmp = intersection(normLine, test_line)
                print(test_line, "point", tmp)
                intersections.append((tmp, i == j))
            intersections.sort()
            # print(intersections)

            d = 0
            for p, bol in intersections:
                if bol:
                    if p[0] > point[0]:
                        d = 1
                    else:
                        d = -1

            valid = []
            for p, bol in intersections:
                if d == 1:
                    if point[0] > p[0]:
                        valid.append(p)
                else:
                    if point[0] < p[0]:
                        valid.append(p)

            print(valid)

# t_x1, t_y1, t_x2, t_y2, t_x3, t_y3, t_x4, t_y4 = [int(x) for x in input().split()]
#
# coords = [(t_x1, t_y1), (t_x2, t_y2), (t_x3, t_y3), (t_x4, t_y4)]
# triangle(coords)

for _ in range(n):
    t_x1, t_y1, t_x2, t_y2, t_x3, t_y3, t_x4, t_y4 = [int(x) for x in input().split()]

    coords = sorted([(t_x1, t_y1), (t_x2, t_y2), (t_x3, t_y3), (t_x4, t_y4)])
    triangle(coords)

    if slope1(coords):
        if triangle(coords):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

