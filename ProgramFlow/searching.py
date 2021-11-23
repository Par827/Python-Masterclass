shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albaross"
found_at = None

# for index in range (6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(1, 21):
    print(i)
    if i > 0 and i % 3 == 0 and i % 5 == 0:
        continue

# using continue
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
