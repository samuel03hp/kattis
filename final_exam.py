'''
n questions, 1 to n
The answer to each one is A, B, C, or D

Answer sheet
n lines
The i-th line contains the answer to question number i

Each question has only one correct answer
1 point per correct question
-------------------------------------------------------------
Hanh wrote the answer for the 2nd question on the 1st line, 
the 3rd uestion on the 2nd line and so on

The n-th line is empty

The answer for the 1st question is not written anywhere

If all answers were on the correct line, they would all be correct
-------------------------------------------------------------
Input
The first lite contains a single int n (1<=n<=1000) 
- the number of questions

n lines follow, the i-th line contains a single character,
A, B, C or D
- the correct answer for the i-th question
-------------------------------------------------------------
Output
Print a single integer - Hanhs final score
-------------------------------------------------------------
Sample input 1
4
A
A
A
A

Sample output 1
3

All questions had A as the correct answer, 
so Hanh wrote A on oll lines
-------------------------------------------------------------
Sample input 2
6
A
D
B
B
C
A

Sample output 2
1
-------------------------------------------------------------
Only if two questions in a row have the same answer, 
Hanh will be correct

He can have maximum n-1 points
'''

n = 0
correct_score = []

hanhs_score = []
hanhs_score.append("X")

final_score = 0

n = int(input())

for i in range(n):
    temp = input()
    correct_score.append(temp)
    if n!= 0:
        hanhs_score.append(temp)

for i in range(n):
    if correct_score[i] == hanhs_score[i]:
        final_score = final_score + 1

print(final_score)