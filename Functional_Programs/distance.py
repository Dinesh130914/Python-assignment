import math


def distance():
    try:
        x = int(input("Enter the value of X :\n"))
        y = int(input("Enter the value of Y :\n"))
    except ValueError:
        print("Please enter numeric value")

    value = (math.pow(x, 2)) + (math.pow(y, 2))
    dis = math.sqrt(value)
    print("Euclidean distance from the point (x, y) to the origin (0, 0) is", dis)


distance()
