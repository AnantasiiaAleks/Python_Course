def fib(n):
    if n in [1, 2]:  # базис
        return 1     # базис
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range (1, 10):
    list_1.append(fib(i))
print(list_1)