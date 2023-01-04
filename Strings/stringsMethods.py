# Using inbuilt methods
# Lets declare Strings
course = 'Python for Beginners'
# Calculating the length of a string using len()
print(len(course))

# converting course into uppercase and lowercase
print(course.upper())
print(course.lower())
# finding the characters in a string to print out their index
print('The index is: ', course.find('y'))

# handling replace functions
print(course.replace('Beginners', 'Absolute Beginner'))

# returns every first letter of the word is capitalizes
print(course.title())

# acts as a checking or a search bar in a sentences which will return True or False
print("Python" in course)
