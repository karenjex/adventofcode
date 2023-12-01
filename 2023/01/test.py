s = 'ab1cde'

def reverse_string(string_in):
    r_string=''
    for char in reversed(string_in):
        r_string+=char
    return r_string

rs = reverse_string(s)

print(s)
print(rs)

