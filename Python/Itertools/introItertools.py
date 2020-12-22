# itertools: product, permutations, combinations, accumlate, groupby, and infinite iterators
#product
from itertools import product
a = [1,2]
b = [3,4]
#prod = product(a,b) # wil compute the cartesian product
prod = product(a,b, repeat=2)
print(list(prod))

#permutations
from itertools import permutations
c = [1,2,3]
#perm = permutations(c) # wil compute the permutations
perm = permutations(c,2)
print(list(perm))

#combinations
from itertools import combinations, combinations_with_replacement
d = [1,2,3,4]
comb = combinations(d,2) # wil compute the combinations (length is mandatory)
print(list(comb))
comb_wr = combinations_with_replacement(d,2)
print(list(comb_wr))

#accumlate
from itertools import accumulate
import operator
e = [1,2,3,4]
#acc = accumulate(e)
acc = accumulate(e, func=operator.mul)
print(e)
print(list(acc))

#groupby
from itertools import groupby

def smaller_than_3(x):
    return x < 3

f = [1,2,3,4]
group_obj = groupby(f, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

#infinite iterators
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break