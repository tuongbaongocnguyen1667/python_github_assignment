#Welcome message
print("Welcome to my Python program!")
#Define variables
hours = input("How many hours did you study today? ")
#Type conversion and calculation
hours = float(hours)
weekly_hours = hours * 7
#Print the output
print(f"You are on track to study {weekly_hours} hours this week.")
#Handling simple error
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()