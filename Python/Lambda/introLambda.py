#lamda arguments:expression
add = lambda x: x + 10
print(add(5))

def add_func(x):
    return x + 10

points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D, key= lambda x: x[1])

print(points2D)
print(points2D_sorted)

#map(func,seq)
a = [1,2,3,4,5,6,7,8]
b = map(lambda x: x*2,a)
print(list(b))

#reduce(func,seq)
from functools import reduce
c = reduce(lambda x,y: x*y,a)
print(c)