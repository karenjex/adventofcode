
a = [1,1,3,1]
b = [1,1,5,1]

def check(l,r,status):
    print("Initial status:",status)
    if status=='u':
        if type(l)==int and type(r)==int:
            if l<r:                                # if left is less than right - pair is in correct order - stop checking
                status='g'   # good
                print("Status (should be good):",status)
                return status
            elif l>r:                              # left is more than right - pair is *NOT* in correct order - stop checking
                status='b'   # bad
                print("Status (should be bad):",status)
                return status
        else:
            for i in range(4):
                l_val=l[i]
                r_val=r[i]
                check(l_val,r_val, status)

print(check(a,b,status))