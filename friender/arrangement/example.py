from time import sleep

def summa(a, b):
    sleep(5)
    return a + b

def mul(a, b):
    yield from  summa(a, b)
    yield

# GIL
# garbage collector

print(summa(1, 5))
print(mul(1, 5))
