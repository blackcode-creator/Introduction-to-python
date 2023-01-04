temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
# >, <, ==, <= >= != these are the comparison operator

# Exercise:
name = input("enter your name: ")
name_length = len(name)
if name_length < 3:
    print("name must be at least 3 characters")
elif name_length > 50:
    print("name can be a maximum of 50 characters")
print("name looks good!")
