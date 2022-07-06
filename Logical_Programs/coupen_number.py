import random

class CouponNumber():

    def __init__(self, take_number):
        self.take_number = take_number

    def calculateDistinctNumber(self):

        distict_number = []
        for x in range(take_number):
            rand = random.randrange(take_number)
            if rand not in distict_number:
                distict_number.append(rand)
            else:
                pass
        return distict_number


while True:
    try:
        take_number = int(input("Enter the distinct number : "))
        if take_number < 0:
            print("Please Enter Positive Digits")
        coupon_number_object = CouponNumber(take_number)
        total_random_number = coupon_number_object.calculateDistinctNumber()
        print(" Distinct Coupon Number : ", total_random_number)

    except ValueError:
        print("Exception Occured,Please numeric value")

