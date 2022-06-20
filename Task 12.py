



def shift(c, d):
    global x
    global y
    x += c
    y += d

def shift_3D(c, d, e):
    global x
    global y
    global z
    x += c
    y += d
    z += e


'''
# Example 1
a = '8'*70

while '2222' in a or '8888' in a:
    if '2222' in a:
        a = a.replace('2222', '88', 1)
    else:
        a = a.replace('8888', '22', 1)

print(a)
'''

'''
# Example 1 (version 2)
a = '8'*70

while '2222' in a or '8888' in a:
    a = a.replace('2222', '88', 1)
    a = a.replace('8888', '22', 1)

print(a)
'''

'''
# Example 2
a = '2' + '5'*81

while '25' in a or '355' in a or '4555' in a:
    a = a.replace('25', '4', 1)
    a = a.replace('355', '2', 1)
    a = a.replace('4555', '3', 1)

print(a)
'''

'''
# Example 2 (version 2)
a = '2' + '5'*81

while '25' in a or '355' in a or '4555' in a:
    for x, y in {"25": '4', "355": '2', "4555": '3'}.items():
        a = a.replace(x, y, 1)

print(a)
'''


'''
# Example 3
s = '1' + '0'*33

while '1' in s:
    if '100' in s:
        s = s.replace('100', '0001', 1)
    else:
        s = s.replace('1', '00', 1)

print(s.count('0'))
'''

'''
# Example 4
s = '1'*46 + '2'*31

while '1111' in s:
    s = s.replace('1111', '2', 1)
    s = s.replace('222', '1', 1)

print(s)
'''

'''
# Example 5

def f(s):
    while '66' in s:
        s = s.replace('66', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '6', 1)
    return s

for i in range(50, 1, -1):
    if f('6'*i) == '21':
        print(i)
        break
'''

'''
# Example 6
s = '>' + '1'*11 + '2'*12 + '3'*30
#s = '>' + '4'*50

while '>1' in s or '>2' in s or '>3' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)

s = s.replace('>', '')
print(sum(list(map(int, s))))
'''

'''
# Example 7
s = '0' + '1'*17 + '2'*11 + '3'*6

while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '302', 1)
    s = s.replace('02', '3103', 1)
    s = s.replace('03', '20', 1)

print(s)
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))
'''

'''
# Example 8
s = '112'*4 + '11'*2

while '11' in s:
    if '112' in s:
        s = s.replace('112', '7', 1)
    else:
        s = s.replace('11', '3', 1)

print(sum(list(map(int, s))))
'''

'''
# Example 9
s = '9992'*33 + '2'*15 + '1'*14
#s = '9'*100 + '2'*48 + '1'*14

while '999' in s or '22' in s:
    if '99' in s:
        s = s.replace('999', '12', 1)
    else:
        s = s.replace('22', '1', 1)

print(s.count('1'))
'''

'''
# Example 10
# подсчитаем количество уникальных значений

for i in range(1, 100):
    s = '5'*i
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    print(s)
'''

'''
# Example 11
# пришлость опять анализировать :(
# в цикле должен осуществиться сдвиг (-15; +30)
# мы можем прибавлять к x единицу, а к y двойку, таким образом получим максимальный n
# учтём уже имеющийся сдвиг внутри цикла и вычислим необходимые a и b

x = 0
y = 0
a = -16
b = -20
n = 15

shift(-7, -1)
for _ in range(n):
    shift(15, 22)
    shift(a, b)
shift(23, -32)

print(x, y)
'''

'''
# Example 12
# в цикле происходит преобразование (+53; -26)
# по имеющемуся значению a вычисляем количество необходимых итераций
# далее подбираем b

x = 0
y = 0
b = 2
n = 5

shift(3, -6)
for _ in range(n):
    shift(4, b)
    shift(6, -6)
shift(-53, 26)

print(x, y)
'''

'''
# Example 13
# проверив, как изменяется x приходим к выводу, что необзодимо 6 итераций
# подбираем b
x = 0
y = 0
b = 20
n = 6

shift(-3, -5)
for _ in range(n):
    shift(2, b)
    shift(8, -12)
shift(2, 3)

print(x, y)
'''

'''
# Example 14
x = 0
y = 0
a = -25
b = -5
n = 4

shift(-5, 15)
for _ in range(n):
    shift(5, 1)
    shift(a, b)
shift(90, 4)

print(x, y)
'''

'''
# Example 15
x = 0
y = 0
z = 2

a = 3
b = 6
c = 5

shift_3D(4, 8, 10)
for _ in range(4):
    shift_3D(2, -4, -5)
    shift_3D(a, b, c)

print(x, y, z)
'''

'''
# Example 19

a = 'КАРА'
i = len(a)
k = 1
b = 'Т'
while i > 1:
    c = a[i-1]
    b += a[i-1]
    i -= k

print(b)
'''



# Example 20
a = 'ИНФОРМАТИКА'
m = 10
b = a[m-1]
for k in (4, 5):
    c = a[k-1]
    b += c

for k in range(1, 4):
    c = a[k-1]
    b += c

print(b)



























