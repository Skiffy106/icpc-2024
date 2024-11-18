n = int(input())

for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(x) for x in input().split()]

    coords = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    slopes = []
    for i, cord1 in enumerate(coords):
        for j, cord2 in enumerate(coords):
            if i == j:
                continue
            x1, y1 = cord1
            x2, y2 = cord2
            if x2 == x1:
                slopes.append(10 ** 5)
                continue
            slope = float(y2 - y1) / float(x2 - x1)
            slopes.append(slope)
    
    valid =  not all(slopes[0] == slopes[i] for i in range(1, len(slopes)))

    if valid:
        print("Yes")
    else:
        print("No")

