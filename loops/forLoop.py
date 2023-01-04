# Here we are going to talk about for loops and ranges
# Declaring a placeholder for the string which is item
for item in 'Python':
    print(list(item))
print('*' * 6, 'new concept', '*' * 6)
# Iteration through the list
for item in ['Mosh', 'Brazil', 'John', 'Smith']:
    print(item)
# Here, we are introducing range function
# range() allows user to generate a series of numbers within a given range

# Examples:
print('*' * 6, 'new concept', '*' * 6)
for i in range(10):
    print(i)
# Here we are including range inbetween example 1 to 5 or 5 to 10
print('*' * 6, 'new concept', '*' * 6)
for i in range(5, 10):
    print(i)

# printing even numbers using range
print('*' * 6, 'new concept', '*' * 6)
for i in range(2, 20, 2):
    print(i)
# Finding the total of elements in the list
print('*' * 6, 'new concept', '*' * 6)
item = [10, 20, 30]
total = 0
for i in item:
    total += i
print(f'Total: {total}')

# Question 2:
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
print('*' * 6, 'Question', '*' * 6)
for i in list1:
    print(i)
# Question 3:
print('*' * 6, 'Question', '*' * 6)
multiplier = int(input('\nenter a number the find multiplication table: '))
up_to = int(input("enter the length of the multiplier: "))
for i in range(1, up_to):
    total = multiplier * i
    print(f'{i} x {multiplier} = {total}')
# Question 4:

print('*' * 6, 'Question', '*' * 6)
grocery = ['bread', 'milk', 'butter']
for index, items in enumerate(grocery):
    print(f'index {index} : {items}')

# Question 5:
print('*' * 6, 'Question', '*' * 6)
n = int(input('enter the nth number: '))
total = 0
for i in range(1, n):
    total += i
print(f'The sum is: {total}')

# Question 6:
print('*' * 6, 'Question', '*' * 6)
for i in range(3, 6):
    print(i, end=',')




