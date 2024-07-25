# List -- []
# A list can store heterogeneous data , different data types in a single list
# Strings are immutable in python that is they are not changable.
# Lists are mutable - they can be changed or modified.

marks = [99.4,45,78,42.5]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
# List Slicing -- <list_name>[starting_index,end_index] # ending index not included.
print(marks[1:3]) # end index not included.
print(marks[0:])
print(marks[:4])
print(marks[-3:-1])


student = ['John',18,96]
print(student)
print(type(student))
student[0] = "Manoj"
print(student)
# print(student[4]) --- Gives out of bounds error.
