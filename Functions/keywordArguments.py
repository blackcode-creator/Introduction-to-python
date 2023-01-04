
# Keyword arguments doesn't worry about position
# mostly to used on numerical parameters passed through a function by prefixing using meaningful words

def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}')
    print('welcome to Python course')


greet_user(last_name="Smith", first_name="John")
