def cust_cost(unit):
    unit = round(unit + unit*.2, 2)
    return unit

def cost():
    pc = input("Enter the cost of the PC: ")
    pc_cost = cust_cost(pc)
    
    dock = input("Enter the cost of the dock: ")
    dock_cost = cust_cost(dock)

    cables = input("Enter the cost of the cables: ")
    cables_cost = cust_cost(cables)

    monitors = input("Enter the cost of the monitors: ")
    monitors_cost = cust_cost(monitors)

    accessories = input("Enter the cost of all miscellaneous accessories: ")
    accessories_cost = cust_cost(accessories)

    total = pc_cost + dock_cost + cables_cost + monitors_cost + accessories_cost
    print(" The cost of the PC is {}.\n The cost of the dock is {}.\n The cost of the cabling is {}.\n The cost of the monitors is {}.\n The cost of all other accessories is {}.\n The total is {}".format(pc_cost, dock_cost, cables_cost, monitors_cost, accessories_cost, total))

cost()

"""
if pc >= 0:
    print(f"The cost of the pc is {pc}")
else:
    pass

if dock >= 0:
    print(f"The cost of the dock is {dock}")
else: 
    pass

if cables >= 0:
    print(f"The cost of the cables is {cables}")
else: 
    pass

if monitors >= 0:
    print(f"The cost of the monitors is {monitors}")
else: 
    pass

if accessories >= 0:
    print(f"The cost of the accessories is {accessories}")
else: 
    pass

print(f"The total is {total} before tax.")
"""






