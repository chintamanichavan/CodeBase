
def reverseString(input_string):
    reverse_string = ""
    char_at_i = ''
    for i in (len(input_string) - 1,0,-1):
        char_at_i = input_string[i]
        reverse_string = reverse_string + char_at_i
    print(reverse_string)

#input_string = input("Enter the input String: ")
input_string = 'jef'
reverseString(input_string)
