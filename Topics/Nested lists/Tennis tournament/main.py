# initialisation
vainqueurs = []

number_of_players = int(input())

# on conserve les vainqueurs dans la saisie au fil de l’eau
for name in range(number_of_players):
	data = input()
	player = data.split(" ")
	if player[1] == "win":
		vainqueurs.append(player[0])

# sortie
print(vainqueurs)
print(len(vainqueurs))
