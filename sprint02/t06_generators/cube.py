def cube(num):
    while num > 0:
        cubed = num * num
        yield cubed * num
        num -= 1

