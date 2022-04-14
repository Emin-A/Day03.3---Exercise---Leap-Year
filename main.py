# Leap Year Exercise 
# Normal year has 365 days , Leap year with and extra day in February 366 days
# On every year that is evenly divisible by 4,                        not a leap year 
#   "except" every year that  "and if it is evenly divisible by 100"  still not a leap year!
#     "unless" the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#   print("Its a leap year!")
# elif year % 100 == 0:
#   print("Not a leap year!")
# elif year % 100 != 0:
#   pass
# elif year % 400: 
#   print("Still a leap year!")
# else:
#   print("Still not a leap year!")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year!")
    else:
      print("Still not a leap year!")
  else:
    print("Leap year!")
else:
  print("Not a leap year!")