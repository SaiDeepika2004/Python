# To check if a number is even or odd :
num = int(input("num : "))
if(num % 2 == 0):
    print("Even number")
else:
    print("Odd number")
# Another easy and effective logic is :
if(num & 1 == 0):
    print("Even number")
else:
    print("Odd number")