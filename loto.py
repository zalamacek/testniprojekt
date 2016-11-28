import random

print "Welcome to the Lottery numbers generator."

amount = int(raw_input("Please enter how many random numbers would you like to have: "))

for number in range(1, amount+1):
    random_number = random.randint(0, 45)
    print random_number






