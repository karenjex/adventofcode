# Goal: Find number of characters that must be processed before the first message marker is detected

# A message marker is a sequence of 14 characters that are all different in the datastream
# Identify the first position where the 14 most recently received characters were all different. 

inputfile = "input.txt"
num_chars=0                # track number of characters to end of first start-of-packet marker
current_buffer=[]          # track latest 14-characters

with open(inputfile) as f:
    while 1:
        # read by character
        char = f.read(1)
        if not char:
            break
        print("Char to process: ",char)
        print("Current buffer length:",len(current_buffer))
        if len(current_buffer)<14:
            current_buffer.append(char)
            print("new_buffer:",current_buffer)
        elif len(current_buffer)==14:
            matched=False
            for i in range(0,14):                # 2 loops to compare each char in current_buffer against the others to find any matches
                for j in range(i+1,14):
                    if current_buffer[i]==current_buffer[j]:
                        matched=True
            print(matched)
            if matched==True:
                # remove first entry from current_buffer and add char to the end
                current_buffer.pop(0)
                current_buffer.append(char)
                print("new_buffer:",current_buffer)
            else:
                # char is not in current_buffer, we have identified the end of the first marker - stop and return num_chars
                break
        num_chars+=1

print("Number of characters processed:",num_chars)