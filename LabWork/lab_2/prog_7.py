'''
**Write a program that receives a list of tuples representing (x, y) coordinates.
Determine whether the points form a straight line.**

'''

def is_straight_line(points):
    x1, y1 = points[0]
    x2, y2 = points[1]

    for i in range(2, len(points)):
        x3, y3 = points[i]

        
        if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
            return False

    return True

raw = input("Enter coordinates : ")
points = [eval(p) for p in raw.split()]


if is_straight_line(points):
    print("The points lie on a straight line.")
else:
    print("The points do NOT lie on a straight line.")
