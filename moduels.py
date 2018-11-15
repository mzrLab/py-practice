# A module is a python file which contains some python definitions and statements.
# usually the module's name with the suffix .py is appended .

# let's write some code : 

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    
#don't panic it's just a module for fibonacci bs
# and then when you import that module it will run the script (the module is actually a script)

>>> import fibo
