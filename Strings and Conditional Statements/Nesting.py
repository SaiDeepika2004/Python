# Nested if's --- an if inside an if

age = int(input())
if(age >= 18):
    if(age >= 80):
        print("cannot Drive")
    else:
        print("Can Drive")
else :
    print("can not drive")
