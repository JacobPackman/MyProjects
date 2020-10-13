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
    
    onsite_labor = input("Enter estimated onsite labor hours: ")
    if onsite_labor == "":
        onsite_cost = 0
    else:
        onsite_cost = float(onsite_labor) * 125


    total_material = pc_cost + dock_cost + cables_cost + monitors_cost + accessories_cost
    total_trip = total_material + 250 + 65 + onsite_cost

    if pc_cost > 0:
        print("\n\n\tThe cost of the PC is ${:.2f}".format(pc_cost))
    if dock_cost > 0:
        print ("\tThe cost of the dock is ${:.2f}".format(dock_cost))
    if cables_cost > 0:
        print("\tThe cost of the cables is ${:.2f}".format(cables_cost))
    if monitors_cost > 0:
        print("\tThe cost of the monitors is ${:.2f}".format(monitors_cost))
    if accessories_cost > 0:
        print("\tThe cost of all other accessories is ${:.2f}".format(accessories_cost))
    print("\tThe total cost of materials is ${:.2f}".format(total_material))
    print("\tThe estimated time onsite would be {} hours and the charge for that is ${:.2f}".format(onsite_labor, onsite_cost))
    print("\tThe total cost of provisioning, trip charge and onsite labor is ${:.2f}".format(total_trip))
        
cost()
