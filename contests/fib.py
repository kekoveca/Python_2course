def fib(n):
    if n - 1 in (0,1):
        return n - 1
    return fib(n - 1) + fib(n - 2)

def fib_loop(n):
    F1 = 0
    F2 = 1
    if n in (1,2):
        return n - 1
    for i in range(2, n):
        sum = F1 + F2
        F1 = F2 
        F2 = sum
    return F2

print(fib_loop(int(input())))