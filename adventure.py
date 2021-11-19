available_exits = ["north", "west", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

print("aren't you glad you got out of there")