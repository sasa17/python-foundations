import datetime
from datetime import date
today = date.today() 


year = input("Enter year of birth:")
month = input("Enter month of birth:")
day = input("Enter day of birth:")
birthday = date(year = int(year), month = int(month), day = int(day))

def check_birthdate(year, month, day):
	if today > birthday:
		return True
	else:
		return False

def calculate_age(year, month, day):
	from datetime import date, timedelta
	age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
	print("Your age is", age, "years old")

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print("Invalid date")