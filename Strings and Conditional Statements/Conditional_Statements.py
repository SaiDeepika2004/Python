# if - elif - else
# age = int(input())
# if(age >= 18):
#     print("Can vote and apply for licensce.")
#     print("can drive")
#     print("can vote")
# else:
#     print("can't vote and drive.")
#     print("Can't apply for driving licensce.")

num = int(input())
# if(num > 2):
#     print("number grater than 2")
# if(num > 3):
#     print("number grater than 3")
     
if(num > 2):
    print("number grater than 2")  # indentation is required.
elif (num > 3):
    print("number grater than 3")
# There is a difference between if and elif statements when if-elif used then if if is right elif is not executed.
else:
    print("The number is less than 2 & 3.")