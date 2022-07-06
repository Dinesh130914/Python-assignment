num = int(input("Enter the number :"))

if 0 < num < 32:
    for i in range(num):
        value = pow(2, i)
        print("2^"+str(i)+" is :"+str(value))
else:
    print("Please enter the valid input")
