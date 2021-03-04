def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    elif sorted(s) == sorted(t):
        return True
    else:
        return False
        