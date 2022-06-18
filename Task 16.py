# kompege

from functools import *

'''
# Example 1
def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 2
    return F(n-1)*F(n-3)

print(F(7))
'''

'''
# Example 2
def F(n):
    if n <= 3:
        return n
    if n % 3 == 0:
        return n*n*n + F(n-1)
    if n % 3 == 1:
        return 4 + F(n//3)
    if n % 3 == 2:
        return n*n + F(n-2)

print(F(100))
'''

'''
# Example 3
def F(n):
    if n <= 10:
        return n
    if n <= 36:
        return n//4 + F(n-10)
    return 2*F(n-5)

print(F(100))
'''

'''
# Example 4
def F(n):
    if n == 1:
        return 2
    if n > 1:
        return F(n-1) + 5*n**2

print(F(39))
'''

'''
# Example 5
def F(n):
    if n < 5:
        return 1 + 2*n
    if n % 3 == 0:
        return 2*(n+1)*F(n-2)
    return 2*n + 1 + F(n-1) + 2*F(n-2)

print(F(15))
'''

'''
# Example 6
def F(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return 3*n + F(n-1)
    return 2*F(n-2)

print(F(31))
'''

'''
# Example 7
def F(n):
    if n <= 3:
        return 3
    if n % 2 == 0:
        return F(n//2) + 5
    return F(n-1) - F(n-2)

print(F(20))
'''

'''
# Example 8
def F(n):
    if n in (1,2):
        return n
    if n > 2:
        if n % 2 == 0:
            return int((n + F(n-2))/5)
        return int((2*n + F(n-1) + F(n-2))/4)

print(F(50))
'''

'''
# Example 9
def F(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n/2 + F(n-1) + 2
    return F(n-1) + 3*n**2

print(F(49))
'''

'''
# Example 10
def F(n):
    if n == 1:
        return 1
    return F(n-1) - n*G(n-1)

def G(n):
    if n == 1:
        return 1
    return F(n-1) + 2*G(n-1)

print(G(18))
'''

'''
# Example 11
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    return  F(n-1) - 2*G(n-1)

def G(n):
    if n == 1:
        return 1
    return F(n-1) + G(n-1) + n

print(sum(map(int, str(G(36)))))
'''

'''
# Example 12
@lru_cache(None)
def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return F(n-1) - F(n-2) + 3*n

print(F(40))
'''

'''
# Example 13
def F(n):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return (n//3)*F(n//3) + n - 12
    return F(n-1) + n*n + 5

c = 0
for n in range(1, 1001):
    a = F(n)
    state = 1
    for i in map(int, str(a)):
        if i%2:
            state = 0
            break
    c += state
print(c)
'''

'''
# Example 14
def F(n):
    if n > 30:
        return n*n + 5*n + 4
    if n % 2 == 0:
        return F(n+1) + 3*F(n+4)
    return 2*F(n+2) + F(n+5)

c = 0
for n in range(1, 1001):
    if sum(map(int, str(F(n)))) == 27:
        c += 1

print(c)
'''

'''
# Example 15
def F(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return F(n/2)
    return 1 + F(n-1)

c = 0
for n in range(1, 501):
    if F(n) == 8:
        c += 1

print(c)
'''

'''
# Example 16
def F(n):
    if n == 1:
        return 1
    if n >= 2:
        if n % 2 == 0:
            return F(n/2) + 1
        return F(n-1) + n

n = 0
while True:
    if F(n) == 19:
        print(n)
        break
    n += 1
'''

'''
# Example 17
c = 0
def F(n):
    global c
    c += 1
    if n >= 1:
        c += 1
        F(n-1)
        F(n-3)
        c += 1

F(40)
print(c)
'''

'''
# Example 18
c = 0
def F(n):
    global c
    c += n*n
    if n > 1:
        c += 2*n + 1
        F(n-2)
        F(n//3)

F(100)
print(c)
'''

'''
# Example 19
def F(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + F(n/3)
    return n + F(n+3)

n = 0
while True:
    try:
        if F(n) >= 100:
            print(n)
            break
    except RecursionError:
        print('Error', n)
    n += 1
'''

'''
# Example 20
def F(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return F(n-2) + n - 2
    return F(n+2) + n + 2

n = 0
c = 0
while True:
    try:
        a = F(n)
        if 10000 <= a <= 99999:
            c += 1
        elif a >= 100000:
            break
    except RecursionError:
        ...
    n += 1

print(c)
'''