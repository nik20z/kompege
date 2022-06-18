# Task 2

def F(*args):
    not_w = not w
    return not(not(z and not_w) or ((z <= w) == (x <= y)))


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w):
                    print(x, y, z, w)


'''
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
                if F(x, y, z):
                    print(x, y, z)
'''
