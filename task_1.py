
def isEven_1(value):
    return value % 2 == 0


def isEven_2(value):
    return value & 1 == 0


if __name__ == '__main__':
    import timeit

    print(timeit.timeit('isEven_1(8)', setup="from __main__ import isEven_1"))
    print(timeit.timeit('isEven_2(8)', setup="from __main__ import isEven_2"))