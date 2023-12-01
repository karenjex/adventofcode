# Goal: Find the total size of the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 

# The total disk space available to the filesystem is 70000000. 
# To run the update, you need unused space of at least 30000000. 

# free_space = 70000000 - total_size_used
# space_to_reclaim = 30000000 - free_space = total_size_used - 40000000

inputfile = "input.txt"
total_size=0

current_dir=[]     # empty if "/", otherwise list of directories in order
dir={"path":[],"size":0}     # store full path and size for each directory
dirs=[]    # list of "dir"
files=[]

with open(inputfile) as f:
    for line in f:
        # print("processing line:",line)
        words=line.split()                        # split line on blank space into separate words
        if words[0]=="$":                         # if first word is "$", this is a command
            if words[1]=="cd":                    #     if 2nd word is "cd", check 3rd word for dir to change to
                if words[2]=="..":                #         If 3rd word is "..", remove last entry from current_dir (ie move up a level)
                    current_dir.pop()
                    # print("current directory:",current_dir)
                elif words[2]=="/":               #         If 3rd word is "/", remove all elements from current_dir (ie move to root)
                    current_dir=[]     
                    # print("current directory:",current_dir)
                else:                             #         3rd word is a directory name: append to current_dir
                    current_dir.append(words[2])
                    # print("current directory:",current_dir)
            # elif words[1]=="ls":    # if 2nd word is "ls", the following lines contain contents of current_dir
                # print("list contents of",current_dir)
        else:                                     # doesn't start with "$": Line contains contents of current_dir
        #     if words[0]=='dir':                   #     if first word is "dir": current_dir contains a directory (name found in 2nd word) 
        #         current_dir.append(words[1])      #         Create a dir entry in dirs for current_dir.append(words[1])
        #         dir={"path":current_dir,"size":0}
        #         print(dir)
        #         dirs.append(dir)
        #         current_dir.pop()
            if words[0]!='dir':                    # If 1st word is a number, ie file size to be added to dir.size
                filesize=int(words[0])
                # else:
                file_exists=False
                for (file) in files:
                    if file['path']==current_dir:
                        file_exists=True
                        file['size']+=filesize
                if not(file_exists):
                    filepath=[]
                    for dir in current_dir:
                        filepath.append(dir)
                    file={"path":filepath,"size":int(words[0])}
                    files.append(file)


max_depth=0
for (file) in files:
    depth=(len(file['path']))
    if depth>max_depth:
        max_depth=depth

dir_totals=[]
total_used=0

for i in range(max_depth+1):
   for (file) in files:
        if len(file['path'])==max_depth-i:
            # print(file)
            file_exists=False
            if len(dir_totals)>0:
              for (dir) in dir_totals:
                  if dir['path']==file['path']:
                      file_exists=True
                      dir['size']+=file['size']
            if not(file_exists):
                # print("adding",file,"to dir_totals")
                filesize=file['size']
                filepath=[]
                for p in file['path']:
                    filepath.append(p)
                dir_totals.append({'path':filepath,'size':filesize})
            if len(file['path'])>0:
                file['path'].pop()
            else: total_used+=file['size']

print("total used",total_used)
space_needed=total_used-40000000
print("additional space needed",space_needed)

space_reclaimed=0
for dir in dir_totals:
    dir_size=int(dir['size'])
    if dir_size>=space_needed:
        if dir_size < space_reclaimed or space_reclaimed==0:
                space_reclaimed=dir_size

print("space reclaimed",space_reclaimed)
