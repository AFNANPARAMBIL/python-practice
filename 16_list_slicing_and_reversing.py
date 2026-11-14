"""Practice slicing, counting and three ways of reversing lists."""

nums = list(range(1, 11))
print("First three:", nums[:3])
print("Last three:", nums[-3:])

values = [2, 5, 2, 7, 2, 9]
print("Count using count():", values.count(2))
count = 0
for value in values:
    if value == 2:
        count += 1
print("Count using loop:", count)

items = [1, 2, 3, 4, 5]
print("Reversed by slicing:", items[::-1])
reversed_copy = items.copy()
reversed_copy.reverse()
print("Reversed by reverse():", reversed_copy)
print("Reversed by reversed():", list(reversed(items)))

sample = [1, 2, 3, 4, 5]
print("Middle slice:", sample[1:4])
print("Last two:", sample[-2:])
print("Every second element:", sample[::2])
