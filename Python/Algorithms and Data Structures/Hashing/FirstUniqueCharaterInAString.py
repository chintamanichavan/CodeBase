
import collections
def firstUniqChar(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    # build hash map : character and how often it appears
    count = collections.Counter(s)
    
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            print(idx)
            return idx     
    return -1

s = "dad"
firstUniqChar(s)