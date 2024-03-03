def DaysOfWeek(day_number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 0 <= day_number <= 6:
        return days[day_number]

day_number = int(input("Enter a day number (0-6): "))
print("Day name:", DaysOfWeek(day_number))
