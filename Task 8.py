from itertools import product, permutations


'''
# Example 3
c = 0
for x in product('ПУЛЯ', repeat=6):
    s = ''.join(x)
    if s.count('У') == 2:
        c += 1

print(c)
'''

'''
# Example 4
c = 0
for x in product('ЛОДКА', repeat=4):
    s = ''.join(x)
    if s.count('О') >=2:
        c += 1

print(c)
'''

'''
# Example 5
# внимательней с условием, потому что буква 'О' должна быть в любом случае!!!
c = 0
for x in product('САЛО', repeat=6):
    s = ''.join(x)
    if 1 <= s.count('О') <= 3:
        c += 1

print(c)
'''

'''
# Example 6
def check_letters(word):
    for i in 'ИГРОК':
        if word.count(i) != 1:
            return False
    return True

c = 0
for x in product('ИГРОК', repeat=5):
    s = ''.join(x)
    if s[0] != 'К' and 'РОК' not in s and check_letters(s):
        c += 1

print(c)
'''

'''
# Example 7
# алгоритм работает очень долго (15-20 с)

def f(x):
    s = ''.join(x)
    for i in glas_letters:
        if s.count(i) == 1:
            s = s.replace(i, '1')
        else:
            return False
    for i in sogl_letters:
        if s.count(i) == 1:
            s = s.replace(i, '0')
        else:
            return False
    return s

c = 0
glas_letters = 'АИОУ'
sogl_letters = 'БКЛН'

for x in product('АБИКОЛУН', repeat=8):
    s = f(x)
    if s != False and '00' not in s and '11' not in s:
        c += 1

print(c)
'''

'''
# Example 8
c = 0
for x in product('AB123', repeat=8):
    s = ''.join(x)
    for i in ('A', 'B'):
        s = s.replace(i, '0')
    if s.count('0') == 2:
        c += 1

print(c)
'''

'''
# Example 9
# необходимо внимательнее читать задание!!!
c = 0
for x in product('01234', repeat=6):
    s = ''.join(x)
    if s[-1] not in '01' and s[0] not in '34':
        c += 1

print(c)
'''

'''
# Example 10
c = 0
for x in product('ВИШНЯ', repeat=6):
    s = ''.join(x)
    if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] not in 'ИЯ':
        c += 1

print(c)
'''

'''
# Example 11
c = 0
for x in product('1234', repeat=4):
    s = ''.join(x)
    if int(s) == int(''.join(sorted(s))):
        c += 1

print(c)
'''

'''
# Example 12
c = 0
for x in product('ГЕПАРД', repeat=5):
    s = ''.join(x)
    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
        c += 1

print(c)
'''

'''
# Example 13
# заметим, что в порядке возрастания у трёхзначных числел нули не могут быть ведущими
# иначе получим 001, а 120 быть не может
c = 0
for x in product('123456789', repeat=3):
    s = ''.join(x)
    if s[0] <= s[1] <= s[2]:
        c += 1

print(c)
'''

'''
# Example 14
c = 0
letters = 'ДЕЙКСТРА'

def check_count_one_letters(s):
    for i in letters:
        if s.count(i) > 1:
            return False
    return True

for x in product(letters, repeat=6):
    s = ''.join(x)
    if check_count_one_letters(s):
        if s.count('Й') == 1 and s[-1] != 'Й' and s[s.index('Й')+1] in 'ДЙКСТР':
            c += 1

print(c)
'''

'''
# Example 15

c = 0
letters = 'ВАЙФУ'

def check_count_one_letters(s, letters):
    for i in letters:
        if s.count(i) > 1:
            return False
    return True

for x in product(letters, repeat=4):
    s = ''.join(x)
    if check_count_one_letters(s, letters):
        if s[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
            c += 1

print(c)
'''

'''
# Example 16
# 8! / (2!*3!)
print(len(set(permutations('МИМИКРИЯ'))))

'''

'''
# Example 17
c = 1
for x in product('ЕЛМРУ', repeat=4):
    s = ''.join(x)
    if s[0] == 'Л':
        print(c)
        break
    c += 1
'''

'''
# Example 18
a = list(product('АГИЛМОРТ', repeat=4))[::-1]
c = len(a)
for x in a:
    s = ''.join(x)
    if s[-2:] == 'ИМ':
        print(c)
        break
    c -= 1
'''


'''
# Example 19
c = 1
for x in product('АИМРЯ', repeat=4):
    s = ''.join(x)
    if s == 'АРИЯ':
        print(c)
        break
    c += 1
'''

'''
# Example 20
print(''.join(list(product('АИМРЯ', repeat=4))[211-1]))
'''

