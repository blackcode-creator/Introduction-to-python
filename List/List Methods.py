
# List Methods operations:
numbers = [5, 2, 1, 7, 4, 20]
# Appending an element without considering the index:
numbers.append(30)
# Adding an element to a specific index
numbers.insert(0, 50)
# Removing an element
numbers.remove(1)
# Sorting the list
# By default: sorting it will be done in ascending order
numbers.sort()
# We make descended list by reverse the list from sort
numbers.reverse()
print(numbers)
print(50 in numbers)


# New concept:
a = [1, 2, 3, 5, 6, 7]
# Copying feature - copies are not tampered after copy
b = a.copy()
a.append(10)
print(f'first list: {a}')
print(f'copied list: {b}')

# write a program to remove the duplicate in a list:
digits = [1, 1, 3, 3, 4, 5, 7, 8]
print(digits)
for i in digits:
    if digits.count(i) == 2:
        digits.remove(i)
        print(digits)

# solution

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

