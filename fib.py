def fib(number):
    i = 0
    j = 1

    for m in range(number):
        yield i
        temp = i
        i = j
        j = temp + j


for x in fib(20):
    print(x)
