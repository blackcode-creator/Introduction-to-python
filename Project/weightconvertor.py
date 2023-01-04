
weight = int(input("Weight: "))
option = input("(L)bs or (K)g: ")

if option == 'L' or option == 'l':
    print(f'You are {weight * 0.45} pounds')

elif option == 'K' or option == 'k':
    print(f'You are {weight / 0.45} Kilograms')
else:
    print("Invalid input")
