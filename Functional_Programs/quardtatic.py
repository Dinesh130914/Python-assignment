import math

value = 1

while value == 1:
    try:
        a = int(input("Enter the value of a :\n"))
        b = int(input("Enter the value of b :\n"))
        c = int(input("Enter the value of c :\n"))
        if a < 0 or b < 0 or c < 0:
            raise ValueError

        if (b > a) & (b > c):
            delta = b * b - 4 * a * c;
            print("Value of delta is ", delta)
            val = int(math.sqrt(delta))
            first_root = ((-b + val) / (2 * a))
            print("Value of Root 1 of X is ", first_root)
            second_root = ((-b - val) / (2 * a))
            print("Value of Root 2 of X is ", second_root)
        else:
            print("Kindly give greater value of b than a and c")
            break
    except ValueError:
        print("Enter the positive number")
    break
