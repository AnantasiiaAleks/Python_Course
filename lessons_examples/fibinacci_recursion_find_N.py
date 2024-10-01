'''
Найти N-е число в последовательности Фибоначчи
0 1 1 2 3 5 8 13 21
'''

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input())

print(fib(n - 2))