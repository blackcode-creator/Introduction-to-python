# Here are going to handle conversion of inputted datatype
# Python always takes any input as a string so, we use different inbuilt function to make conversion as follows
# int(), float(), type(), str()
# so, lets give the age by converting age from year
# can only concatenate str using + (not "float")
birth_year = input('Your birth year: ')
# here, the input is a string we need to convert it to integer
age = 2022 - int(birth_year)
# Printing the output after conversion
print(age)

# Conversion weight in pound to Kilograms
weight_lbs = input("Weight in pounds: ")
weight_kg = int(weight_lbs) * 0.45
print("weight in kgs: ", weight_kg)
