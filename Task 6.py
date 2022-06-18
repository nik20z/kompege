
'''
#Example 11
for s in range(100, 0, -1):
   n = 1024
   a = s
   while s >= 5:
       s = s - 5
       n = n // 2
   if n == 64:
       print(a)
       break
'''

'''
#Example 12
for s in range(80, 1, -1):
   n = 1
   a = s
   while s <= 80:
       s = s + 7
       n = n * 3
   if n == 81:
       print(a)
       break
'''

'''
#Example 13
for s in range(94):
   n = 1
   a = s
   while s < 94:
       s = s + 8
       n = n * 2
   if n == 128:
       print(a)
       break
'''

'''
#Example 14
for s in range(45, 0, -1):
   n = 1
   a = s
   while s <= 45:
       s = s + 4
       n = n * 2
   if n == 256:
       print(a)
       break
'''

'''
#Example 15
c = 0
for d in range(223, 2019):
   n = 27
   s = 12
   while s <= 2019:
       s = s + d
       n = n + 16
   if n == 171:
       c += 1
print(c)
'''

'''
#Example 16
a = []
for d in range(100):
   d_start = d
   n = 1
   while d // n > 0:
       d = d - 2
       n = n + 3
   if n == 46:
       a.append(d_start)
print(a)
'''

'''
#Example 17
for s in range(220, 10, -1):
   s_start = s
   n = 3
   while s < 220:
       s = s + 6
       n = n + 3
   if n > 40:
       print(s_start)
       break
'''

'''
#Example 18
c = 0
for s in range(9, 100):
   n = 3
   while s * n < 243:
       s = s // 3
       n = n * 9
   if n == 27:
       c += 1
print(c)
'''

'''
#Example 20
for s in range(0, 10000):
   s_start = s
   n = 100
   while s - n >= 100:
       s = s + 20
       n = n + 40
   if s_start != s:
       print(s_start)
       break
'''