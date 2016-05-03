def fibonacci(n):
    j = k = 1
    yield j
    yield k
    for i in range(n):
        yield j + k
        if i % 2 == 0:
            j = j + k
        else:
            k = j + k


def caching(func):
    cache = {}
    def cache_func(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return cache_func


@caching
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)


# %time fibonacci(100)
# CPU times: user 3 us, sys: 1e+03 ns, total: 4 us

# %time fib_recursive(100)
# CPU times: user 185 us, sys: 174 us, total: 359 us

def main():
    print fib_recursive(100)
    print list(fibonacci(100))[99]

if __name__ == '__main__':
    main()
