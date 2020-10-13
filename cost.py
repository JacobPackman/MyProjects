def cust_cost(unit):
    unit = round(unit + unit*.2, 2)
    return unit

def cost():
    pc = input("Enter the cost of the PC: ")
    if pc == "":
        pc = 0
        pc_cost = 0
    else:
        pc_cost = cust_cost(float(pc))

    dock = input("Enter the cost of the dock: ")
    if dock == "":
        dock = 0
        dock_cost = 0
    else:
        dock_cost = cust_cost(float(dock))

    cables = input("Enter the cost of the cables: ")
    if cables == "":
        cables = 0
        cables_cost = 0
    else:
        cables_cost = cust_cost(float(cables))

    monitors = input("Enter the cost of the monitors: ")
    if monitors == "":
        monitors = 0
        monitors_cost = 0
    else:
        monitors_cost = cust_cost(float(monitors))

    accessories = input("Enter the cost of all miscellaneous accessories: ")
    if accessories == "":
        accessories = 0
        accessories_cost = 0
    else:
        accessories_cost = cust_cost(float(monitors))

    total = pc_cost + dock_cost + cables_cost + monitors_cost + accessories_cost
    
    if pc_cost > 0:
        print("\n\n\tThe cost of the PC is ${}".format(pc_cost))
    if dock_cost > 0:
        print ("\tThe cost of the dock is ${}".format(dock_cost))
    if cables_cost > 0:
        print("\tThe cost of the cables is ${}".format(cables_cost))
    if monitors_cost > 0:
        print("\tThe cost of the monitors is ${}".format(monitors_cost))
    if accessories_cost > 0:
        print("\tThe cost of all other accessories is ${}".format(accessories_cost))
    print("\tThe total is ${}".format(total))
        
cost()