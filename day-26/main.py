# # # List Comprehension

# numbers = [1, 2, 3]
# -> Uzun ve Geleneksel Yol
# new_numbers = []
# for n in numbers:
#     new_item = n + 1
#     new_numbers.append(new_item)
#
# -> Kısa ve Modern Yol
# new_numbers = [n + 1 for n in numbers]
#
# #Yazdırma
# print(new_numbers)
#
# -> String için yapımı (Harflerine ayırdırk!)
# name = "Eren"
# list_name = [letter for letter in name]
# print(list_name)
#
# mylist = range(1, 5)
# new_list = [2*n for n in mylist]
# print(new_list)
#
# names = ["Eren", "Osman", "Ece", "Mustafa", "Hasan", "Sema", "Ali"]
# short_names = [name.upper() for name in names if len(name) < 5]
# print(short_names)




# # # Dictionary Comprehension

# import random
# names = ["Eren", "Osman", "Ece", "Mustafa", "Hasan", "Sema", "Ali"]
# students_score = {student : random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student : score for (student, score) in students_score.items() if score>=50}
# print(passed_students)

# # # With Pandas Dataframe

student_dict = {
    "student": ["Eren", "Ece", "Osman"],
    "score": [51, 99, 70]
}
import pandas

student_dataframe = pandas.DataFrame(student_dict)
print("===================================")
print(student_dataframe)
print("===================================")
# for (key, value) in student_dataframe.items():
#     print(key)

for (index, row) in student_dataframe.iterrows():
    print(row.student)

