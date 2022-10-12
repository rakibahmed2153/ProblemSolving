a = input('Enter string === \n')
b = input('Enter the character === \n')
c = ''

for index in a:
    if(index != b):
        c = c + index
print('Result -->', c)
