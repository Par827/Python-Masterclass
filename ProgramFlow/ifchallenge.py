name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome {} to the party!".format(name))
else:
    print("Sorry... you are {} and don't meet our requirements.".format(age))
print("-" * 100)