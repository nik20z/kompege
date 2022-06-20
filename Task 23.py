


# дефолтный шаблон для увеличения
def f_plus(start, stop, exc = []):
    if start > stop or start in exc:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return count_prog(f_plus, start, stop, exc=exc)


# шаблон для варианта для уменьшения
def f_minus(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    if start > stop:
        return count_prog(f_minus, start, stop)


'''
# Example 1
count_prog = lambda f, start, stop: f(start+1, stop) + f(start+3, stop) + f(start*2, stop)
print(f_plus(1, 15))
'''

'''
# Example 2
count_prog = lambda f, start, stop: f(start+1, stop) + f(start*2, stop) + f(start**2, stop)
print(f_plus(5, 154))
'''

'''
# Example 3
count_prog = lambda f, start, stop: f(start+1, stop) + f(start+2, stop) + f(start*4, stop)
print(f_plus(1, 13))
'''

'''
# Example 4
count_prog = lambda f, start, stop: f(start-2, stop) + f(start-5, stop)
print(f_minus(23, 2))
'''

'''
# Example 5
count_prog = lambda f, start, stop: f(start-1, stop) + f(start-3, stop) + f(start//3, stop)
print(f_minus(22, 2))
'''

'''
# Example 6
count_prog = lambda f, start, stop: f(start+1, stop) + f(start*2, stop)
print(f_plus(1, 10) * 2)
'''

'''
# Example 7
count_prog = lambda f, start, stop: f(start+1, stop) + f(start*2, stop)
print(f_plus(1, 12) * f_plus(12, 30))
'''

'''
# Example 8
count_prog = lambda f, start, stop: f(start+1, stop) + f(start+3, stop) + f(start*2, stop)
print(f_plus(3, 9) * f_plus(9, 12) * f_plus(12, 20))
'''

'''
# Example 9
count_prog = lambda f, start, stop: f(start-8, stop) + f(start//2, stop)
print(f_minus(102, 43) * f_minus(43, 5))
'''

'''
# Example 10
# число 6 не может входить в траекторию, поэтому считаем как обычно
count_prog = lambda f, start, stop: f(start+2, stop) + f(start*3, stop)
print(f_plus(1, 25) * f_plus(25, 63))
'''

'''
# Example 11
count_prog = lambda f, start, stop, exc: f(start+1, 
                                           stop, 
                                           exc=exc) + f(start+2, 
                                                        stop, 
                                                        exc=exc) + f(start*3, 
                                                                     stop, 
                                                                     exc=exc)
print(f_plus(4, 8) * f_plus(8, 23, exc=[11, 18]))
'''

'''
# Example 12
count_prog = lambda f, start, stop, exc: f(start+1,
                                           stop,
                                           exc=exc) + f(start*2,
                                                        stop,
                                                        exc=exc) + f(start*2+1,
                                                                     stop,
                                                                     exc=exc) + f(start*10,
                                                                                  stop,
                                                                                  exc=exc)
print(f_plus(1, 15))
'''

'''
# Example 13
count_prog = lambda f, start, stop, exc: f(start+2,
                                           stop,
                                           exc=exc) + f(start*2-1,
                                                        stop,
                                                        exc=exc) + f(start*2+1,
                                                                     stop,
                                                                     exc=exc)
print(f_plus(7, 63, exc=[43]))
'''

'''
# Example 14
def f_double_plus(start, stop):
    start_int = int(start)
    stop_int = int(stop)
    if start_int > stop_int:
        return 0
    if start_int == stop_int:
        return 1
    if start_int < stop_int:
        return count_prog(f_double_plus, start, stop)


plus_one = lambda number: str(format(int(number, 2)+1, 'b'))
count_prog = lambda f, start, stop: f(plus_one(start), stop) + \
                                    f(start+'0', stop) + \
                                    f(start+'1', stop)
print(f_double_plus('100', '11101'))
'''

'''
# Example 15
def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return count_prog(f, start, stop)

def plus_one_digit(number):
    r = ''
    for i in str(number):
        r += str(int(i) + (1 if i != '9' else 0))
    return int(r)

count_prog = lambda f, start, stop: f(start+1, stop) + f(plus_one_digit(start), stop)
print(count_prog(f, 25, 51))
'''

'''
# Example 16
def f(start, stop):
    if start == 'error' or start > stop:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return count_prog(f, start, stop)


second_command = lambda number: number*1.5 if number % 2 == 0 else 'error'
count_prog = lambda f, start, stop: f(start+1, stop) + f(second_command(start), stop)
print(f(1, 20))
'''


# Example 17
