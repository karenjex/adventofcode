
num_digits=[1,4,2,6]

num=0
len_num=len(num_digits)
print(len_num)
for index,digit in enumerate(num_digits):
    print('digit:',digit,'index:',index)
    power=(len_num-1)-index
    val = digit * 10**power
    num+=val


print('number:',num)