import math 
import time

def timer(func):
    def inner(*args, **kwargs):
        print("Time started")
        start = time.time()

        func(*args, **kwargs)

        print("Time ended")
        end = time.time()

        print(f'total time taken: {end-start}')

    return inner

# timer()()

@timer
def get_factorial(n):
    print("Factorial started")

    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')


get_factorial(120)