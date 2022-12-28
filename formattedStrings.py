
# Formatting strings(Prefix Strings)
first = 'John'
last = 'Smith'
# Here, we are not involve formatting functions
message = first + ' [' + last + '] is a coder'
# Let apply, some formatting functions
msg = f'{first} [{last}] is a coder'
print(message)
print('*' * 10, 'after', '*' * 10)
print(msg)
