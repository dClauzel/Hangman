string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

counter = 0
for i in string:
	if i in vowels:
		counter += 1

print(counter)
