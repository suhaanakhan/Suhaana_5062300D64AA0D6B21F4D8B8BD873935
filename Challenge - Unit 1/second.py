year = int(input("Enter the year to be checked: "))
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
  print("Leap Year")
else:
  print("Not a Leap Year")
