import array as arr


def findTriplets(arr, n):
    found = 0
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    found = 1

    if found == 0:
        print(" not exist ")


num = int(input('How many elements you want to check (minimum 3 required)'))
print('The elements are')

for n in range(num):
    element = int(input())
    ar = arr.array('i', [element])

print(len(ar))
findTriplets(ar, len(ar))
