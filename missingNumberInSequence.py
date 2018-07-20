def find_missing_number(sequence):
	listForm = sequence.split()
	if len(listForm) == 0:
		return 0
	listForm.sort()
	prev = listForm.pop(0)
	if not prev.isdigit():
		return 1
	if int(prev) == 2:
		return 1
	print(prev)
	print(listForm)
	for number in listForm:
		if prev.isalpha() or number.isalpha():
			return 1
		elif int(prev) + 1 != int(number):
			return int(prev) + 1
		else:
			prev = number
	return 0
print(find_missing_number("15 11 10 2 13 9 3 1 12 5 6 8 14 4"))