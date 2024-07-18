# Logical operators(and , or, not)
# Precedence order - not,and,or
# Work  on Boolean operators

# not(F)---T , not(T)----F
a = 50
b = 30
print(not False) # True
print(not True)  # False
print(not(a > b)) # False
print(a > b)  # True
print(not(a)) # False
print(not(b)) # False

# and -- T and T = T , T and F = F , F and T = F, F and F = F
# or --- T or T = T, T or F = T, F or T = T, F or F = F

val1 = True
val2 = False
print("and operator : ",val1 and val2)
print("or operator : ",val1 or val2)

print((a==b) or (a>b))
print(not(val1 or a) and val1 or val2)
print(not val1 or a and (val1 or val2))