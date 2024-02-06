num = int(input())
global get_person
get_person = "SK"


def change():
	global get_person
	if get_person == "SK":
		get_person = "CY"
	else:
		get_person = "SK"


if num == 1 or num == 3 or num == 5:
	print(get_person)
	exit()

while True:
	if num == 2 or num == 4:
		change()
		break
	elif num == 1 or num == 3 or num == 5:
		break

	num -= 3
	change()

print(get_person)
