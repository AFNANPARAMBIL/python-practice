"""Calculate travel distance from speed and time."""
speed = float(input("Speed (km/h): "))
time = float(input("Time travelled (hours): "))
if speed < 0 or time < 0:
    print("Speed and time cannot be negative.")
else:
    print("Distance travelled:", speed * time, "km")
