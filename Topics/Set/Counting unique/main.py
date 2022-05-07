# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
all_the_students = Belov + Smith + Sarada
my_set = set(all_the_students)
print(len(my_set))
