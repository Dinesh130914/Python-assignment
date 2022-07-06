num = int(input("How many number of series you want"))

har = 1
for i in range(2, num):
    har += 1 / i
else:
    print('The Harmonic series is :', har)
