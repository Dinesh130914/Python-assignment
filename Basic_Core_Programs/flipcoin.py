import random

rang = int(input('How many times yo to flip the coin'))
head = 0
tail = 0

for i in range(rang):
    coin = random.randint(0, 1)
    print(coin)
    if coin == 0:
        head += 1
    else:
        tail += 1
else:
    headpercentage = int(head * 100 / rang)
    print('Head Percentage is : ' + str(headpercentage)+'%')
    tailpercentage = int(tail * 100 / rang)
    print('Tail Percentage is : ' + str(tailpercentage)+'%')
