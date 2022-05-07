# put your python code here
nb1 = float(input())
nb2 = float(input())
opérateur = input()


def non_null(a):
	if a == 0.0:
		print("Division by 0!")
		exit()


def plus(a, b):
	return a + b


def moins(a, b):
	return a - b


def diviser(a, b):
	non_null(b)
	return a / b


def multiplier(a, b):
	return a * b


def modulo(a, b):
	non_null(b)
	return a % b


def division_entière(a, b):
	non_null(b)
	return a // b


def puissance(a, b):
	return a ** b


if opérateur == "+":
	print(plus(nb1, nb2))
elif opérateur == "-":
	print(moins(nb1, nb2))
elif opérateur == "/":
	print(diviser(nb1, nb2))
elif opérateur == "*":
	print(multiplier(nb1, nb2))
elif opérateur == "mod":
	print(modulo(nb1, nb2))
elif opérateur == "pow":
	print(puissance(nb1, nb2))
elif opérateur == "div":
	print(division_entière(nb1, nb2))
