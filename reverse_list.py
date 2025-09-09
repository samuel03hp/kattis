'''
Name on Kattis: Öfugsnúið

Jóna needs a program. The program should read in integers and 
print them in reverse order. Jóna asks for your help.

Input
The first line contains the integer. Then there is a list of 
integers, each on their own line. Each integer will be between 
and.

Output
Print the list in the reverse order compared to the input.
'''

n = 0

array = []

n = int(input())

for i in range(n):
    temp = input()
    array.append(temp)

array.reverse()

for i in range(n):
    print(array[i])