def fibonaqi(n):
    if n < 2:
        return n
    else:
        return fibonaqi(n-1)+fibonaqi(n-2)


if __name__ == "__main__":

    n = int(input('第几个数？\n'))
    # print(n)
    print(fibonaqi(n-1))
