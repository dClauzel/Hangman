raw_text = input()  # get values in a string
words = raw_text.split(" ")  # turn the string into a list of strings
words_title = [x.title() for x in words]  # set the first letter of all words from the list to a capital letter
words_title[0] = words_title[0].lower()  # set the first letter of the first word from the list to a low letter
print("".join(words_title))  # turn the list into a string
