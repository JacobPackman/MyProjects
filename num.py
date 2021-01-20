def print_halves(num):
    if num % 2 == 0:
        a = int((num / 2))
        b = int((num / 2))
        return a, b
    else:
        a = int(((num - 1) / 2 ))
        b = int(((num + 1 ) / 2))
        return "[{}], [{}]".format(a, b)
print(print_halves(49))