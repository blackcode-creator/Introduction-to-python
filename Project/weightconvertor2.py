weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f'You are {weight * 0.45} kilos')
else:
    print(f'You are {weight / 0.45} pounds')
