def sum_ch(a, b):
    return a + b
def fib(n):
    a, b = 0, 1
    result=[]
    while a < n:
        result.append(a)
        a, b = b, a + b
        return result
def max_ch(x, y):
    return max(x, y)