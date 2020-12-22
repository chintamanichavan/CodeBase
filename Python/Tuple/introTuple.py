# Ordered, Immutable, allows duplicate elements
myTuple = ("Max", 28, "Boston") #parenthesis are optional
print(myTuple) # if you want to define a single element in a tuple add a comma in after defining the tuple

import sys
myList = ["Max", 28, "Boston"]
print(sys.getsizeof(myList), "bytes")
print(sys.getsizeof(myTuple), "bytes")

#working with tuples can be more efficient than working with tuples
# it uses less memory and is faster than the list
