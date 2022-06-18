from functools import *
# 2, 7, 9, 10

'''
# Example 1
def F(x_small, a, b):
    global x
    while x_small > 0:
        a = a + 1
        if x_small % 11 > b:
            b = x % 11
        x_small = x_small // 11
        if a == 7 and b == 7:
            print(x)
            return True
    return False
x = 1
while True:
    a = 0
    b = 0
    if F(x, a, b):
        break
    x += 1
'''


# Example 2
# суть алгоритма заключется в том, что
# число x содержит в себе остатки от деления на 4
# произведение которых равно 24, а сумма 16, причём цифры располагаются в порядке убывания
# это позволит получить наибольший x
#x = int(input())
x = 0
for i in [3,2,2,1,1,1,1,1,1,1,1,1]:
    x *= 4
    x += i
print(x)

a = 2
b = 3
while x > 0:
    d = x % 4
    a *= d
    if d < 3:
        b += d
    x //= 4

print(a, b)



'''
# Example 3
def F(x_small, a, b):
    global x
    a = 0
    b = 0
    while x_small > 0:
        a += 1
        if x_small % 2 != 0:
            b += 1
        x_small //= 2
    if a == 16 and b == 14:
        return True
    return False

x = 1
c = 0
while True:
    a = 0
    b = 0
    if F(x, a, b):
        c += 1
    x += 1
    print(c)
'''

'''
# Example 4
def F(x, y, a, b):
    while x*y > 0:
        if x > 0:
            a += 1
        if y > 0 and y % 7 > b:
            b = y % 7
        x //= 10
        y //= 7
    if a == 4 and b == 5:
        return True
    return False

# заметим, что для получения a=4,
# необходимо произвести 4 итерации при x>0
# x //= 10 проходит после прибавления a += 1
x = 10**3
for y in range(10000):
    a = 0
    b = 0
    if F(x, y, a, b):
        print(x*y)
        break
'''

'''
# Example 5
# проанализируем: чтобы получить a=6, необходимо провести 6 итераций с x//2
# но т.к. счётчик находится до x//2, то мы находим x=2*5=32
# для y аналогично, только при //10 необходимо провести 7 итераций: y=10**6

x = 32
y = 10**6
print(x*y)
a = 0
b = 0
while x > 0 or y > 0:
    if x > 0:
        a += 1
    if y > 0:
        b += 1
    x //= 2
    y //= 10
print(a, b)
'''

'''
# Example 6
# проанализировав алгоритм приходим к выводу,
# что из N вычитается прогрессия
# максимум можем провести 9 итераций, причём, последнее условие на чётность не проходит
# и мы получаем ответ 9
# d = 3, T1 = 3
# S = (2*T1 + d*(n-1))/2*n
# S = (2*3 + 3*(9-1))/2*9 = 135

N = 135
c = 0
T = 3
d = 3
while N != 0:
    N -= T
    T += d
    c += 1

if c % 2 == 0:
    c += d

print(c)
'''


'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Example 7

T = int(input())
c = 0
N = 0
d = 5
while N <= 300:
    N += T
    T += d
    c += 1

if c % 2 != 0:
    c += d

print(c)
'''

'''
# Example 8
x = 100
while True:
    x += 1
    L = x - 18
    M = x + 36
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    if M == 9:
        print(x)
        break
'''

'''
# Example 9
x =

a = 5*x + 245
b = 5*x - 807
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)

1052
'''
