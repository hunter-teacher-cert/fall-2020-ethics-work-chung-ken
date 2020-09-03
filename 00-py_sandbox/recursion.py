# Clyde "Thluffy" Sinclair
# Aug 2020

def factorial(n):
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

print("Good News Everyone!")
print(f"4! = {factorial(4)}" )
print(f"fib(5) = {fib(5)}" )

