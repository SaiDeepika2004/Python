# Ternary operator / Single if Statements : <var> = <value1> if <condition> else <val2>
food = input("food : ")
eat = "Yes" if (food == "cake" or food == "Cake") else "No"
print(eat)
# <str1> if <condition> else <str2>
food_new = input("food : ")
print("sweet") if food_new == "cake" or food_new == "jalebi" else print("not sweet")

# Clever If - A type of ternary operator
# <var> = (false_value,true_value) [<condition>]

age = int(input("age : "))
# Clever if:
# vote = ("yes","no") [age < 18]
# print(vote)

# Single If: 
vote = "Yes" if age >=18 else "No"
print(vote)

# Example 2 :
sal = float(input("Salary : "))
tax = sal*(0.1,0.2) [sal > 50000]
print(tax)