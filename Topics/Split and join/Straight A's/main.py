raw_scores = input()

grades = raw_scores.split(" ")
number_of_A = grades.count("A")
number_of_grades = len(grades)

percent_of_A = round(number_of_A / number_of_grades, 2)
print(percent_of_A)
