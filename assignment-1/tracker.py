# Name: Abhinav Krishna
# Roll no.: 2501730114
# Date: 10th Nov, 2025
# Project: Daily Calorie Tracker

import datetime

print("DAILY CALORIE TRACKER")
print("Enter your today's meals, count if you are in your daily limit,")
print("by telling us your daily calorie limit.\n")
print("Stay healty and Stay safe")

meals = []
calories = []

num_meals = int(input("How many no. of meals did you have taken today? "))

for i in range(num_meals):
    meal_name = input("\nEnter meal {} name: ".format(i + 1)).strip()
    meal_cal = float(input("Enter calories for meal {}: ".format(meal_name)))
    meals.append(meal_name)
    calories.append(meal_cal)


if len(calories) > 0:
    total_calories = sum(calories)
    average_calories = total_calories / len(calories)
else:
    total_calories = 0
    average_calories = 0

daily_limit = float(input("\nEnter your daily calorie limit : "))

if total_calories > daily_limit:
    status = "WARNING: You have crossed your daily calorie limit!"
elif total_calories == daily_limit:
    status = "PERFECT! You met your target exactly."
else:
    status = "GOOD JOB! You are within your daily limit."


print("\n TODAY'S CALORIE SUMMARY ")
print("{:<18}{}".format("Meal", "Calories"))
print("--------------------------------------------")
for meal, cal in zip(meals, calories):
    print("{:<18}{}".format(meal, cal))
print("--------------------------------------------")
print("Total Calories:\t{}".format(total_calories))
print("Average/Meal:\t{:.2f}".format(average_calories))
print("--------------------------------------------")
print(status)


save_log = input("\nDo you want to save this report? (yes/no): ").lower().strip()

if save_log == "yes":
    file_name = "calorie_log_" + str(datetime.date.today()) + ".txt"
    file = open(file_name, "w", encoding="utf-8")

    file.write("===== DAILY CALORIE TRACKER LOG =====\n")
    file.write("Date & Time: " + str(datetime.datetime.now()) + "\n\n")
    file.write("{:<18}{}\n".format("Meal", "Calories"))
    file.write("--------------------------------------\n")

    for meal, cal in zip(meals, calories):
        file.write("{:<18}{}\n".format(meal, cal))

    file.write("--------------------------------------\n")
    file.write("Total Calories:\t{}\n".format(total_calories))
    file.write("Average/Meal:\t{:.2f}\n".format(average_calories))
    file.write("--------------------------------------\n")
    file.write(status + "\n")

    file.close()
    print("\nReport saved successfully as '{}'.".format(file_name))
else:
    print("\nNo report saved. Have a great day!")
