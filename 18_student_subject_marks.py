"""Calculate average and percentage for six subjects (200 marks each)."""
subjects = ["English", "Maths", "Arabic", "Chemistry", "Physics", "Biology"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks for {subject} (out of 200): "))
    if not 0 <= mark <= 200:
        print("Marks must be between 0 and 200.")
        break
    marks.append(mark)
else:
    total = sum(marks)
    print(f"Average marks: {total / len(subjects):.2f}")
    print(f"Percentage: {total / 1200 * 100:.2f}%")
