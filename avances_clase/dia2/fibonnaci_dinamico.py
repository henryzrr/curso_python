def fibonacci():
    def fib_intern(n):
        ls=[0 for i in range(n+1)]
        ls[1]=ls[2]=1
        for i in range(3,n+1):
            ls[i]=ls[i-1]+ls[i-2]
        return ls
    return fib_intern

fibb = fibonacci()
print(fibb(10))