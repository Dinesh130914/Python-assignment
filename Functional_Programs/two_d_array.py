import array as arr

row = int(input('enter the rows'))
col = int(input('enter the column'))

i = 0

print('enter the elements')
while i < row:
    j = 0
    while j < col:
        element = int(input(str(i)+","+str(j) + "value is :"))
        ar = arr.array('i', [element])
        j += 1

    i += 1

for i in range(len(ar)):
    for j in range(len(ar)-1):
        print(ar[i, j], end="")

    print("")

