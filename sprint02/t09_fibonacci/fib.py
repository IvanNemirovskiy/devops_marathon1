def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

def fib_generator(n: int) -> int:
    i = 0

    while i < n:
       yield fib(i)
       i +=1
