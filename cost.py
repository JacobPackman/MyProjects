def cust_cost(unit):
    unit = round(unit + unit*.2, 2)

def cost(pc,dock,cables,monitors,accessories):
    pc = input("Enter the cost of the PC")
    pc_cost = cust_cost(pc)
    
    dock = input("Enter the cost of the dock")
    dock = cust_cost(dock)

    cables = input("Enter the cost of the cables")
    cables = cust_cost(cables)
    
    monitors = input("Enter the cost of the monitors")
    monitors = cust_cost(monitors)

    accessories = input("Enter the cost of all miscellaneous accessories")
    accessories = cust_cost(accessories)

    total = pc + dock + cables + monitors + accessories

cost(pc,dock,cables,monitors,accessories)

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







