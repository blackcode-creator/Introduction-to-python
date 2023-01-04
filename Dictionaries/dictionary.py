
# Used to information which has key value pair
# Example of key value pair is as follows:
# Name: John Smith
# Email: john@gmail.com
# Phone: 0791660287
# Defining a dictionary
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
# Access the dictionary using a square brackets
# dictionary are case-sensitive
print(customer['name'])
print(customer.get('name'))

# Updating
customer['name'] = 'jack line'
print(customer['name'])

# Creating a program to generate numbers in word form:
digits = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
phone = input('Phone number: ')
output = ""
for ch in phone:
    output += digits.get(ch, '!') + ' '
print(output)
