numbers = []
while True:
	data = input()
	if data == ".":
		break
	else:
		numbers.append(float(data))
print(min(numbers))
