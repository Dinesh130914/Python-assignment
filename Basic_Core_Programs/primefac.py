n = int(input("Enter any Number for calculating the prime factors: "))
i = 1

while i <= n:
    flag = 0
    if n % i == 0:
        j = 1
        while j <= i:
            if i % j == 0:
                flag += 1
            j = j + 1

        if flag == 2:
            print(i)
    i = i + 1
