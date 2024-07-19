str = "i am a coder"
print(str.endswith("er")) # returns True if string ends with the given substring
print(str.endswith("ess"))
print(str.capitalize()) 
print(str) # Capitalize only changes str for once not permenantly.
print(str.replace("a","the")) # replace all occurances of old substring with the new one.
print(str.find("Coder")) # C not present so returns -1.
print(str.find("Coder")) # returns first index of the 1 st occurance.
print(str.find("coder")) 
print(str.find("c"))
print(str.find("or"))
print(str.count("am")) # counts the occurance of the sub string in the main string