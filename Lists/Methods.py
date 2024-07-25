# List Methods --- Append,sort,reverse,insert
list = [2,1,3]
print(list)
list.append(4) # add the element at the end
print(list)
list.sort()
print(list)
print(list.sort()) # ascending order
list.sort(reverse=True)
print(list) # descending order
print(list.sort(reverse=True))
list.insert(1,5) # Insert an element at a specific position.
print(list)

list1 = [2,1,3,1]
list1.remove(1) # removes first occurance of the element.
print(list1)
list1.pop(2) # To remove the element at a particular index.
print(list1)

list2 = ["banana","cherry","apple"]
list2.sort()
print(list2)
list2.sort(reverse = True)
print(list2)
list2.insert(2,"grapes")
print(list2)

list3 = [3,5,9,1,0,12,65,32,75,4,5,3,1,12,34,32,1,12,0]
print("List 3 : ",list3)
list4 = list3.copy() # To copy the contents of one list into another list.
print(list4)
print(list3.count(0))
print(list3.count(12))
print(list3.count(1))