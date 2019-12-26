print("Welcome to the special recruitment program, please answer the following questions:")

skills = ["Microsoft Excel", "Microsoft Word", "Microsoft Powerpoint", "Due Diligence"]
cv = {}
name = input("What is your name?")
cv['Name:'] = name
age = input("How old are you?")
cv['Age'] = age
experience = input("How many years of experience do you have?")
cv['Experience'] = experience
cv['Skills'] = []

print("Skills")
for index, skill in enumerate(skills):
	print(str(index + 1), skill)

skill1 = input("Choose a skill from above by entering its number:")
skill2 = input("Choose another skill from above by entering its number:")

cv['Skills'].append(skills[int(skill1)-1])
cv['Skills'].append(skills[int(skill2)-1])

if int(age) >= 25 and int(age) <= 40 and int(experience) > 3 and (int(skill1) == 1 or int(skill2) == 1):
	print("You have been accepted,", name)
else:
	print("Unfortunately, you do not fit the criteria")