
#Example 19

'''
#Example 1
mas = []
for n in range(1, 100):
   a = format(n, 'b')
   for _ in range(2):
       if a.count('1') % 2:
           a += '1'
       else:
           a += '0'
   a = int(a, 2)
   if a > 80:
       print(a)
       mas.append(a)
print(min(mas))
'''

'''
#Example 2
a = []
for n in range(1, 100):
   r = format(n, 'b')
   r += '10' if n % 2 else '01'
   r = int(r, 2)
   if r > 81:
       a.append(r)
print(min(a))
'''

'''
#Example 3
for n in range(1, 100):
   r = format(n, 'b')
   r += r[-1]
   for _ in range(2):
       r += '1' if n%2 else '0'
   r = int(r, 2)
   if r > 130:
       print(n, r)
       break
'''

'''
#Example 4
>>> 144//8
18
>>> bin(18)
'0b10010'
>>> bin(19)
'0b10011'
>>> int('10011100', 2)
156
'''

'''
#Example 6
for n in range(100, 1, -1):
   r = int(str(int(format(n, 'b')[::-1])), 2)
   if r == 13:
       print(n)
       break
'''

'''
#Example 7
c = 0
for n in range(1, 100):
   r = format(n, 'b')
   for _ in range(2):
       r += str(n % 2)
   r = int(r, 2)
   if r < 80:
       c += 1
print(c)
'''

'''
#Example 8
a = []
for n in range(1, 1000):
   r = format(n, 'b')
   if n % 2:
       r = f"11{r}11"
   else:
       r = f"1{r}0"
   r = int(r, 2)
   if r > 52:
       a.append(r)
print(min(a))
'''

'''
#Example 9
for n in range(10000, 1000, -1):
   n = str(n)
   a = int(n[0]) * int(n[1])
   b = int(n[2]) * int(n[3])
   if f"{a}{b}" in ('1214', '1412'):
       print(n)
       break
'''

'''
#Example 10
for n in range(1000, 100, -1):
   n = str(n)
   a = int(n[0]) * int(n[1])
   b = int(n[1]) * int(n[2])
   c = f"{a}{b}" if a > b else f"{b}{a}"
   if c == '240':
       print(n)
       break
'''



