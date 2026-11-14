"""Analyze total, average, highest and lowest marks."""

marks = [78, 92, 65, 88, 70]
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
print("Total:", total)
print(f"Average: {average:.2f}")
print("Highest:", highest)
print("Lowest:", lowest)
