"""Find the index of the first occurrence of a number in a list."""

nums = [15, 42, 8, 23, 42]
number = int(input("Enter a number: "))
if number in nums:
    print("Found at index", nums.index(number))
else:
    print("Not found")
