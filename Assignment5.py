# Take input from the user of 5 numbers and store it in a list.
lst = list()
for i in range(5):
    lst.append(float(input(f"Enter Number {i+1} : "))) 

# sum
print()
print("Sum of List numbers : ",sum(lst))
# smallest number 
print()
print("Minimum among List numbers : ",min(lst))
# largest number 
print()
print("Maximum among List numbers : ",max(lst))
# ascending order 
print()
lst.sort()
print("List in Ascending order : ",lst)
# desending order 
print()
lst.reverse()
print("List in Desending order : ",lst)
# convert list in tuples 
print()
t = tuple()
t = lst
print("List in Tuple : ",t)
# delete list 
print()
del lst
print("The List is Deleted!")