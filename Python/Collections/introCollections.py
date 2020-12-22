# Collections: Counter, namedTuple, OrderDict, defaultdict, deque
from collections import Counter
a = "aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbvvvvvvvvvvvvvvvvvvvvvvvvv"
print(Counter(a))
print(Counter(a).most_common(1))