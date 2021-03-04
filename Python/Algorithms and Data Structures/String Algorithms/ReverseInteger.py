
def checkConstraints(num): 
    if num == 0:
        return 0
    if num < -65536 or num > 65536:
        return 0
    elif num < 0 or num > 0:
        reverseInteger(num)
    else:
        None

def reverseInteger(num): #34
    reverse_integer = 0
    rem = 0
    if num > 0:
        while num > 0: 
            rem = num % 10 # 4 
            reverse_integer = reverse_integer * 10 + rem 
            num = (int)(num / 10) # 3
    else:
        num = num * (-1)
        while num > 0: 
            rem = num % 10 # 4 
            reverse_integer = reverse_integer * 10 + rem 
            num = (int)(num / 10) # 3
        reverse_integer = (-1) * reverse_integer
    print(reverse_integer)

num = -45
checkConstraints(num)


