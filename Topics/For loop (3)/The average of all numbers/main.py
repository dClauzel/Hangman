# put your python code here
a = int(input())
b = int(input())

somme = 0
compte = 0
for number in range(a, b + 1):
	if number % 3 == 0:
		somme += number
		compte += 1

print(somme / compte)
