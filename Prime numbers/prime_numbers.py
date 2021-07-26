import time


def prime_numbers(n: int) -> list:  # 2.5613227685292563
    pn = [2]
    for i in range(3, n):
        f = True
        for j in pn:
            if not i % j:
                f = False
                break
        if f:
            pn.append(i)

    return pn


def prime_numbers_fast(n: int) -> list:
    class Helper:
        values = {
            2: 0
        }

        @classmethod
        def next(cls):
            for f in cls.values:
                cls.values[f] = (cls.values[f] + 1) % f

        @classmethod
        def add(cls, num: int):
            cls.values[num] = 0

        @classmethod
        def is_prime(cls, num: int) -> bool:
            for f in cls.values:
                if not cls.values[f]:
                    return False
            return True

    for i in range(3, n):
        Helper.next()
        if Helper.is_prime(i):
            Helper.add(i)

    return list(Helper.values.keys())


def test(fun):
    print(f'\nТест {fun.__name__}\n' + '-' * 20)

    n = 10**4
    n_tests = 3
    times = []
    for i in range(n_tests):
        s_time = time.time()
        fun(n)
        f_time = time.time()

        times += [f_time - s_time]
        print(times[-1])

    print('-' * 20)
    print(sum(times) / n_tests)


test(prime_numbers)
test(prime_numbers_fast)

# print(prime_numbers_fast(1000))
