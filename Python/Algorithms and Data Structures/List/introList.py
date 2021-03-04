# Lists: Ordered, mutable, allows duplicate elements
mylist = ["banana","apple","cherry"]
print(mylist)

mylist2 = [5,True,"orange"]

print(mylist2)

# A list can contain different data types

#iterate over the list

for i in mylist:
    print(i)

# checking item in the the list

if "banana" in mylist:
    print("Yes")
else:
    print("No")

# length of the list
print(len(mylist))

#append an item to the list
mylist.append("Orange")
print(mylist)

#insert item at specific position
mylist.insert(1,"blueberry")

#remove item from the last position
item = mylist.pop()
print(item)

#remove a specific item
mylist.remove("cherry")
print(mylist)

#reverse the list
mylist.reverse()
print(mylist)

#sort the list
mylist3 = [-3,8,5,2,-4]
#mylist3.sort()
print(mylist3)

#create a new sorted list
sorted_mylist3 = sorted(mylist3)
print(sorted_mylist3)

#list with duplicate elements
mylist4 = [4] * 7
print(mylist4) 

# adding two lists
mylist5 = mylist + mylist2
print(mylist5)

# slicing the list
mylist6 = mylist5[1:5]
print(mylist6)

#copying of lists
list_org = ["orange","mango","jackfruit"]
#list_copy = list_org  Warning: The reference number for copy_list and original list is same.
list_copy=list_org.copy()

print(list_copy)
list_copy.append("Grapes")
print(list_copy)
print(list_org)

#list comprehension
mylist7 = [i*i for i in mylist3]

print(mylist7)

#dict comprehension

mylist9 = mylist2 + mylist3
print(mylist9)