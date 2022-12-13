# I am going to remind myself on the basic of python
# We can do some mathematical operation
print(3+3)
x = 5
y = 6
print(x+y)
print(x*3)

myEmail = input("Enter your email:")
print("Type your password.")
typedPassord = input()
savedPassword = 'kilo'
if typedPassord == savedPassword:
    print("Congratulations! you are now logged in")
else:
    print("Your password is incorrect. Please try again.")

inbox = 0
while inbox < 10:
    print("you have a message")
    inbox = inbox + 1
name =""
while name!="casanova":
    name = input("Enter your name:")
    print("Congratulation")
i=0
for i in range(10):
    print(i**2)
# adding numbers from one to 100
total = 0
for num in range (101):
    total = total + num
    print(total)