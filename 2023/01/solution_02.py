# GOAL:
#   Recover calibration value from each line of puzzle input and calculate the sum of the values
#   The first and last digit are combined (in that order) to form a two-digit calibration number
#   BUT the digits may be spelled out

# inputfile = "input_test_2b.txt"
inputfile = "input.txt"
f = open(inputfile, "r")

# Define functions

def reverse_string(string_in):
    r_string=''
    for char in reversed(string_in):
        r_string+=char
    return r_string

def get_digit(word_in):
    # Replace spelled out digit with associated integer value
    if word_in=='one':
        digit = 1
    elif word_in=='two':
        digit = 2
    elif word_in=='three':
        digit = 3
    elif word_in=='four':
        digit = 4
    elif word_in=='five':
        digit = 5
    elif word_in=='six':
        digit = 6
    elif word_in=='seven':
        digit = 7
    elif word_in=='eight':
        digit = 8
    elif word_in=='nine':
        digit = 9
    return digit

def find_first_digit(string_in):

    # return value and position of first numeric digit in string
    # if none found, first_digit_index and first_digit will both be -1

    found_first_digit=False
    first_digit_index=-1
    first_digit=-1
    for (index, x) in enumerate(string_in):
        if not found_first_digit and x.isdigit():
            found_first_digit=True
            first_digit=int(x)
            first_digit_index=index
    return first_digit,first_digit_index

def find_last(input_string,words):

    rstring = reverse_string(input_string)

    # reverse_string=reversed(input_string)
    last_digit,last_digit_index = find_first_digit(rstring)   

    if last_digit_index != -1:
        last_digit_index=(len(input_string)-(last_digit_index+1))      # calculate position from start of original string
 
    # get position and value of last spelled digit
    # if none found, last_word_index and last_word_digit will be -1

    last_word=''
    last_word_index=-1
    last_word_digit=-1
    for word in words:
        # if word exists in string, return its position (else return -1)
        # ** THIS RETURNS POSITION OF FIRST OCCURENCE OF GIVEN WORD - WE WANT THE LAST! **
        word_index=rstring.find(reverse_string(word))
        if word_index != -1:
            word_index=(len(input_string)-(word_index+1))      # calculate position from start of original string

        if word_index != -1:
            # word was found in the string. See if it appears later than previously found words
            if last_word_index == -1 or (last_word_index != -1 and word_index > last_word_index):
                # either this is the first word we've found, or it appears later than the other words we've found
                    last_word=word
                    last_word_digit=get_digit(last_word)
                    last_word_index=word_index

    # Return either last word or last digit, whichever is last

    # print("last spelled out number value:",last_word_digit,"index:",last_word_index)
    # print("last digit value:",last_digit,"index:",last_digit_index)

    if last_word_index == -1:
        # no spelled out numbers were found
        return last_digit
    elif last_digit_index == -1:
        # no digits were found
        return last_word_digit
    elif last_digit_index>last_word_index:
        # last digit is laster than last spelled out number
        return last_digit
    else:
        # last_digit_index<last_word_index
        # last digit is earlier than last spelled out number. 
        return last_word_digit

def find_first(input_string,words):

    first_digit,first_digit_index = find_first_digit(input_string)   
 
    # get position and value of first spelled digit
    # if none found, first_word_index and last_word_digit will be -1

    # first_word=''
    first_word_index=-1
    first_word_digit=-1
    for word in words:

        # if word exists in string, return position of first occurence (else return -1)
        word_index=input_string.find(word)
        if word_index != -1:
            # word was found in the string. See if it appears earlier than previously found words
            if first_word_index == -1 or word_index < first_word_index:
                # either this is the first word we've found, or it appears earlier than the other words we've found
                first_word=word
                first_word_digit=get_digit(first_word)
                first_word_index=word_index

    # print("first spelled out number value:",first_word_digit,"index:",first_word_index)
    # print("first digit value:",first_digit,"index:",first_digit_index)

    # Return either first word or first digit

    if first_word_index == -1:
        # no spelled out numbers were found
        return first_digit
    elif first_digit_index == -1:
        # no digits were found
        return first_word_digit
    elif first_digit_index<first_word_index:
        # first digit is earlier than first spelled out number
        return first_digit
    else:
        # first_digit_index>first_word_index
        # first digit is later than first spelled out number. 
        return first_word_digit


cval_total = 0
words = ['one','two','three','four','five', 'six', 'seven', 'eight', 'nine']

for line in f:

    if line != '':
        first_digit=find_first(line,words)
        last_digit=find_last(line,words)
        cval=10*first_digit + last_digit
        print(cval)
        cval_total+=cval

f.close()

print("Sum of calibration values:",cval_total)