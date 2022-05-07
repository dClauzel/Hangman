raw_text = input()
words = raw_text.split("_")
words_cleaned = [x.capitalize() for x in words]
print("".join(words_cleaned))
