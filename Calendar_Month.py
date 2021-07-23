import calendar

year = int(input("Enter the year: "))
if (calendar.isleap(year)):
  print("It is a leap year")
else:
  print("It is not a leap year")