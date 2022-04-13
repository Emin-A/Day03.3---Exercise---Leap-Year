# Leap Year Exercise 
# Normal year has 365 days , Leap year with and extra day in February 366 days
# On every year that is evenly divisible by 4,
#   "except" every year that is evenly divisible by 100
#     "unless" the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  print("Leap year!")
elif year % 100:
  print("Not a leap year!")
elif year % 400:
  print("Still a leap year!")
 