def fibonacci():
    def fibonacci_intern(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            return fibonacci_intern(n-2)+fibonacci_intern(n-1)
    return fibonacci_intern

fib = fibonacci()
print(fib(1))