"""List operations from my Colab practice notebook."""

fruits = ["apple", "banana", "cherry"]
print("Original fruits:", fruits)
fruits.append("mango")
fruits.insert(1, "kiwi")
print("After append and insert:", fruits)
fruits.remove("banana")
print("After remove:", fruits)

nums = [3, 8, 1, 9, 4]
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))
print("Original list:", nums)

values = [10, 20, 30]
values.append([40, 50])
print("After append nested list:", values, "Length:", len(values))
values.extend([60, 70])
print("After extend:", values, "Length:", len(values))

original = [1, 2, 3]
alias = original
alias.append(4)
print("After alias append:", original)
copy_list = original.copy()
copy_list.append(5)
print("Original after copy append:", original)
print("Copy:", copy_list)
