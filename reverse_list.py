n = 0

array = []

n = int(input())

for i in range(n):
    temp = input()
    array.append(temp)

array.reverse()

for i in range(n):
    print(array[i])