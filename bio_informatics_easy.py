dic = {'A':'T','T':'A','G':'C','C':'G'}
string = raw_input('give sequence')
new = ''
for char in string:
    if char in dic:
        new += dic[char]
    else: new += ' ERROR '

print new
