def CountDown(arg):
    count = 0
    num = list(str(arg))
    for i in num:
        if count < 2:
            print(i, end="")
            count += 1
        else:
            print(i,end="-")
            count = 0

raw = input("Enter the number: ")
CountDown(raw)