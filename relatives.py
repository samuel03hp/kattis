'''

How many positive integers less than n are relatively prime to n?

To be reletively prime:
a and b are reletively prime if:

there is no integers 
x >= 2, y >= 1, z >= 1

such that
a = xy and b = xz

Example:
n = 5

5 and b are reletively prime if
there is no integers 
x >= 2, y >= 1, z >= 1

such that
5 = xy and b = xz

Test:
5 is a prime number, 
meaning all integers less than 5 are reletively prime to it

!!All prime numbers n give output n-1!!

Test:
6 and 5 --> 5 is prime, output +1

6 and 4:
6 = 2*3     (x=2, y=3)
4 = 2*2     (x=2, z=2)
--> not reletively prime

!!All pairs of even numbers, output +0!!

!!If n-i is a prime number and n is not divisable by n-1, output+1

Example:
20 and 5
5 is prime, but 20/5=4 --> output +0

'''



import math

def is_prime_func(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break

    return is_prime

temp = 1
list = []

prime_factors = []

while temp!=0:
    temp = int(input())
    if(temp == 0):
        break
    else:
        list.append(temp)

for i in range(len(list)):
    n = list[i]

    if is_prime_func(n):
        print(n-1)
    else:
        m = n

        if m % 2 == 0:
            prime_factors.append(2)

            #divide until odd
            while m % 2 == 0:
                m = m // 2

        #test odd cases up to sqrt(m)
        f = 3
        while f * f <= m:
            if m % f == 0:
                prime_factors.append(f)
                #strip all factors of f
                while m % f == 0:
                    m = m // f
            f += 2
            
        if m > 1:
            prime_factors.append(m)
            
        output = n
        for p in prime_factors:
            output = output // p * (p-1)
            
        prime_factors.clear()
        print(output)
    
