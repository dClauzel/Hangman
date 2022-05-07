x = float(input())
y = float(input())

if x == y == 0:
	print("It's the origin!")
elif x == 0 or y == 0:
	print("One of the coordinates is equal to zero!")
elif 0 < x and 0 < y:
	print("I")
elif x < 0 and 0 < y:
	print("II")
elif x < 0 and y < 0:
	print("III")
else:
	print("IV")

