print("Today is a great day to learn Python!")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "Quotes" in strings')
print("Hello" + " World")
greeting = "Hello"
name = "Zach"
print(greeting + name)

# if we want to space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 Years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])