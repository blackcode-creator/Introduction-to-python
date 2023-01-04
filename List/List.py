# Declaring list of items
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# Updating values
names[0] = 'Samuel'
print(names)

# Write a program to find the largest number in a list
numbers = [1, 3, 4, 67, 32, 45, 90, 87]
Max = numbers[0]
for i in numbers:
    if i > Max:
        Max = i
print(f'Largest number is: {Max}')
