
def convert_in_counting_system_and_counting(x, n, i):
    c = 0
    while x > 0:
        if x % n == i:
            c += 1
        x //= n
    return c

def convert_in_counting_system(x, n, to_int = True):
    b = ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n != 10:
        while x > 0:
            r = x % n
            b += str(r) if r < 10 else alphabet[r-10]
            x //= n
        b = b[::-1]
    else:
        b = str(x)

    if to_int and n <= 10:
        return int(b)
    return b


def sum_digit_in_number(x):
    return sum(list(map(int, str(x))))


'''
# Example 1
x = 64**30 + 2**300 - 4
print(convert_in_counting_system_and_counting(x, 8, 7))
'''

'''
# Example 2
x = 3*16**8 - 4**5 + 3
print(convert_in_counting_system_and_counting(x, 4, 3))
'''

'''
# Example 3
x = 2*27**7 + 3**10 - 9
print(convert_in_counting_system_and_counting(x, 3, 0))
'''

'''
# Example 4
x = 51*7**12 - 7**3 - 22
print(sum(list(map(int, convert_in_counting_system(x, 7, to_int=False)))))
'''

'''
# Example 5
x = lambda i: 125**200 - 5**i + 74

for i in range(1000):
    x_five_system = str(convert_in_counting_system(x(i), 5))
    if x_five_system.count('4') == 100:
        print(i)
        break
'''

'''
# Example 6
# решил аналитически
# например при степени 2015 мы получаем выражение: 4**2015 + 15
# в нём 5 единиц, далее увеличиваем степень и видем прямую зависимость
x = lambda i: 4**2015 + 2**i - 2**2015 + 15
print(convert_in_counting_system(x(2510), 2, to_int=False).count('1'))
'''

'''
# Example 7
x = lambda i: 4**1014 - 2**i + 12
for i in range(2005):
    count = convert_in_counting_system(x(i), 2, to_int=False).count('0')
    if count == 2000:
        print(i)
        break
'''

'''
# Example 8
# подобрал аналитически
x = lambda i: 36**17 - 6**i + 71
# x = lambda i: 6**34 - 6**i + 71 - при i>34 ловим ошибки
b = convert_in_counting_system(x(24), 6)
print(b)
print(sum_digit_in_number(b))
'''

'''
# Example 9
x = 6*144**26 + 11*12**75 - 48
print(str(convert_in_counting_system(x, 12)).count('B'))
'''

'''
# Example 10
#x = 5*216**1156 - 4*36**1147 + 6**1153 - 875
x = 5*6**3468 - 4*6**2294 + 6**1153 - 875

num = convert_in_counting_system(x, 6, to_int=False)
count_five = num.count('5')
count_zero = num.count('0')

print(count_five - count_zero)
'''


'''
# Example 11
for x in range(1, 20):
    try:
        if int('33', x+4) - int('33', 4) == 33:
            print(x)
            break
    except:
        ...

'''

'''
# Example 12
for n in range(1, 20):
    try:
        if int('103', n) == int('97', n+2):
            print(n)
            break
    except:
        ...
'''

'''
# Example 13
for n in range(1, 20):
    try:
        if int('132', n) + 11 == int('124', n+1):
            print(n)
            break
    except:
        ...
'''

'''
# Example 14
for x in range(1, 20):
    try:
        if int('21', x) * int('13', x) == int('313', x):
            print(x)
            break
    except:
        ...
'''

'''
# Example 15
for x in range(21, 30):
    if convert_in_counting_system(x, 3) % 100 == 11:
        print(x)
        break
        
'''

'''
# Example 16
for x in range(41, 1, -1):
    if convert_in_counting_system(x, 2, to_int=False)[-4:] == '1011':
        print(x)
        break
'''

'''
# Example 17
for n in range(2, 20):
    a = convert_in_counting_system(68, n, to_int=False)
    if a[-1] == '2' and len(a) == 4:
        print(n)
        break
'''

'''
# Example 18
for n in range(1, 100):
    num_six = convert_in_counting_system(n, 6, to_int=False)
    if len(num_six) == 2:
        num_five = convert_in_counting_system(n, 5, to_int=False)
        if len(num_five) == 3:
            num_eleven = convert_in_counting_system(n, 11, to_int=False)
            if num_eleven[-1] == '1':
                print(n)
                break
'''

'''
# Example 19
for n in range(1, 100):
    num_seven = convert_in_counting_system(n, 7, to_int=False)
    if len(num_seven) == 2:
        num_six = convert_in_counting_system(n, 6, to_int=False)
        if len(num_six) == 3:
            num_thirteen = convert_in_counting_system(n, 13, to_int=False)
            if num_thirteen[-1] == '3':
                print(n)
                break
'''

'''
# Example 20
c = 0
for n in range(1, 625):
    num_five = convert_in_counting_system(n, 5, to_int=False)
    if len(num_five) <= 4:
        num_double = convert_in_counting_system(n, 2, to_int=False)
        if len(num_double) >= 5:
            num_sixteen = convert_in_counting_system(n, 16, to_int=False)
            if num_sixteen[-1] == 'C':
                c += 1
    else:
        break

print(c)
'''











