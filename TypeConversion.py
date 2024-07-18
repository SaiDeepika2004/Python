# Type Conversion -- Convert a type of variable into an another type of variable
# 2 types -- Type conversion (done automatically by the compiler), Type Casting(Done Forcefully by the developer or done manually)
a = 2
b = 4.25
sum = a+b
print(sum) # Type conversion done implicitly.
print(int(sum)) # Explicit conversion done - Type Casting

a = "2"
b = 2.25
sum = int(a)+b # Forcefully typecating the string a to int variable.
print(sum)
print(int(sum))