"""Find complete student groups and leftover students."""
total_students = int(input("Total students: "))
group_size = int(input("Students per group: "))
if total_students < 0 or group_size <= 0:
    print("Total students must be non-negative and group size positive.")
else:
    print("Complete groups:", total_students // group_size)
    print("Students left over:", total_students % group_size)
