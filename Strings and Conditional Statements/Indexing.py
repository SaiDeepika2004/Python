str = "Katakam Sai Deepika"
print(str[0])
print(str[1])
for i in range(len(str)):
    print(str[i],end = " ")
# We cant replace a charecter in the string like str[4]='@' is not possible.
print()
# Slicing --- Accessing parts of a string by breaking them into parts , Syntax : [start:end]
print(str[1:4])
print(str[0:7])
print(str[:4]) # from starting to final index.
print(str[5:]) # from 5th index to final index.
print(str[-1])
print(str[-3:-1])
print(str[-1:])
print(str[:-1])
print(str[-5:-2])