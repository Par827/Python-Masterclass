#                    1         2
#          012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"

backwords = letters[::-1]
print(backwords)

print(letters[5::-1])

#Excercise
#Create a slice that produces the characters QPO.
backwords = letters[16:13:-1]
print(backwords)
#answer
print(letters[16:13:-1])

#Slice the string to produce EDCBA
backwords = letters[4::-1]
print(backwords)
#answer
print(letters[4::-1])

#Slice the string to produce the last 8 characters, in reverse order
backwords = letters[:-9:-1]
print(backwords)
#answer
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])      #Idiom grabs first letter without crashing
print(letters[0])

