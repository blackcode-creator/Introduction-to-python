# Here using of single quotes and double matters due to the following reasons:
# 1. We use single quotes when there is no possession quotes if there are we use double quotes
# Case 1:
course = "Python's course for Beginners"
print(course)

# Case 2:
course = 'Python for Beginners'
print(course)

# using multiple string to write multiple string in one variable
message = '''
Hi, John Smith
Hope you well 
Thank you

The Technical Team
'''
print(message)

# We can also access characters by using indexing or negative indexing
# We declare index using square brackets

course = "Python course for beginners"
print(course[0])
# accessing index using negative index
print(course[-1])

# accessing the characters by using the ratio example [0:3] it show until the character index [2] which will be pyt
# it will print Pyt
print(course[0:3])
# it will print course
print(course[7:13])
# Here it will print the entire after the start point of index
print(course[7:])
# Quiz what i will be displayed
name = "Jennifer"
print(name[1:-1])


