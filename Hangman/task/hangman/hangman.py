import random

# configuration
mots_possibles = ("python", "java", "swift", "javascript")
nombre_victoires = int(0)
nombre_défaites = int(0)


# jouer une partie
def jouer():

	# initialisation de la partie
	mot_à_trouver = random.choice(mots_possibles)
	masque = list("-" * len(mot_à_trouver))
	lettres_essayées = list()
	vies_restantes = 8

	while vies_restantes > 0:

		# saisie utilisateur si le mot n’est pas trouvé
		if "".join(masque) != mot_à_trouver:
			print("".join(masque))
			essai = input("Input a letter: ")
		else:
			continue

		# saisie utilisateur invalide: >1
		if len(essai) != 1:
			print("Please, input a single letter.\n")
			continue

		# saisie utilisateur invalide: pas dans [a-z]
		if not (essai.islower() and essai.isalpha()):
			print("Please, enter a lowercase letter from the English alphabet.\n")
			continue
		else:
			pass

		# lettre déjà essayée
		if essai in lettres_essayées:
			print("You've already guessed this letter\n")
			pass

		# lettre dans le mot et pas déjà essayée
		if essai in mot_à_trouver and essai not in masque:
			# recherche de la position de la lettre dans le mot, pour l’ajouter au masque
			for position_lettre in range(len(mot_à_trouver)):
				if mot_à_trouver[position_lettre] == essai:
					lettres_essayées.append(essai)
					masque[position_lettre] = essai
			print("")

		# lettre pas dans le mot
		if essai not in mot_à_trouver:
			print("That letter doesn't appear in the word.\n")
			lettres_essayées.append(essai)
			vies_restantes = vies_restantes - 1

		# mot trouvé
		if "".join(masque) == mot_à_trouver:
			print("You guessed the word " + mot_à_trouver + "!")
			print("You survived!")
			global nombre_victoires
			nombre_victoires = nombre_victoires + 1
			return

	# fin while vie_restantes > 0
	else:
		print("You lost!")
		global nombre_défaites
		nombre_défaites = nombre_défaites + 1
		return


# jouer une partie
def résultats():
	print("You won: " + str(nombre_victoires) + " times")
	print("You lost: " + str(nombre_défaites) + " times")
	pass


# main
print("H A N G M A N")
while True:
	choix = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
	if choix == "play":
		jouer()
	elif choix == "results":
		résultats()
	elif choix == "exit":
		exit(0)
	else:
		pass
