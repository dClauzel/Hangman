nombre_de_saisies = int(input())

for _ in range(0, nombre_de_saisies):
	nombre = int(input())
	if nombre % 7 == 0:
		print(nombre * nombre)
