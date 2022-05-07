data = input()

# By construction, the right substring always
# has a greater index than the left one.
# So let’s just focus on it 😃
print(data.rfind("old"))
