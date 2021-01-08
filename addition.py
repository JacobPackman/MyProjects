pc = 1
while pc != "":
    pc = input("Please enter price of machine:\n")
    pc = pc.replace(",","")
    pc = float(pc)
    pc = pc + 250
    print("The cost of the pc is ${:.2f}".format(pc))