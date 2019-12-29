import datetime
from datetime import date
today = date.today() 

class Employees:
	def __init__(self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year
	
	def get_working_years(self):
		return today.year - int(self.employment_year)

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s, Working Years: %s" % (self.name, self.age, self.salary, self.get_working_years())

class Managers(Employees):
	def __init__(self, name, age, salary, employment_year, bonus_percentage):
		super().__init__(name, age, salary, employment_year)
		self.bonus_percentage = bonus_percentage
	
	def get_bonus(self):
		return float(self.bonus_percentage) * float(salary)

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %s" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

employees_list = []
managers_list = []

print("Welcome to HR Pro 2019")

options = ("Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit")
print("Options:")
for index, option in enumerate(options):
	print(str(index + 1), option)

option = int(input("What would you like to do?"))

while option != 5:
	print("---------------")
	if option == 1:
		print("Employees")
		for inputs in employees_list:
			print(inputs)
		print("--------------")
	elif option == 2:
		print("Managers")
		for inputs in managers_list:
			print(inputs)
		print("--------------")
	elif option == 3:
		name = input("Name:")
		age = input("Age:")
		salary = input("Salary:")
		employment_year = input("Employment Year:")
		new_employee = Employees(name, age, salary, employment_year)
		employees_list.append(new_employee)
		print("Employee added succesfully")
		print("--------------")
	elif option == 4:
		name = input("Name:")
		age = input("Age:")
		salary = input("Salary:")
		employment_year = input("Employment Year:")
		bonus_percentage = input("Bonus:")
		new_manager = Managers(name, age, salary, employment_year, bonus_percentage)
		managers_list.append(new_manager)
		print("Manager added succesfully")
		print("--------------")
	print("Options:")
	for index, option in enumerate(options):
		print(str(index + 1), option)
	option = int(input("What would you like to do?"))