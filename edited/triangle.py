#   In solving problem 10 I incorrectly thought that I needed to test if a point lies
#   inside a triangle. Now I want to finish what I started.

def vec_diff(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return x2 - x1, y2 - y1

def cross_product(vec1, vec2):
    x1, y1 = vec1
    x2, y2 = vec2
    return x1 * y2 - y1 * x2

def is_point_in_triangle(point, tri):
    p1, p2, p3 = tri

    # Calculate vectors from the point to each of the triangle's vertices
    v1 = vec_diff(p1, point)
    v2 = vec_diff(p2, point)
    v3 = vec_diff(p3, point)

    cp1 = cross_product(v1, vec_diff(p2, p1))
    cp2 = cross_product(v2, vec_diff(p3, p2))
    cp3 = cross_product(v3, vec_diff(p1, p3))

    all_pos =  all(cp > 0 for cp in (cp1, cp2, cp3))
    all_neg =  all(cp < 0 for cp in (cp1, cp2, cp3))

    if all_pos or all_neg:
        return True
    return False

# Test Cases:
# -5 0
# 5 3 2 10 -6 -3
# -> False

# 0 0
# 2 -2 -4 -2 2 5
# -> True

# See this desmos graph I made
# https://www.desmos.com/calculator/0gcovvzoch
if __name__ == "__main__":
    px, py = [int(x) for x in input().split()]
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]

    test_point = (px, py)
    triangle_vertices = [(x1, y1), (x2, y2), (x3, y3)]

    print(is_point_in_triangle(test_point, triangle_vertices))
