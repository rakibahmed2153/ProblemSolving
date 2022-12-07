'''

Question:
----------
from the array make a key value array. But the year string only take the number year value
Input = [“Java”, “3”, “CSS”, “1 Year”, “JavaScript”, “2 YR”]
Output = Java, 3

'''

input = ['Java', '3', 'CSS', '1 Year', 'JavaScript', '2 YR']
newArr = {}
for i in range(len(input)):
    
    if(i%2 != 0):
        b = input[i].split( )
        newArr[input[i-1]] = int(b[0])
    else:
        a = input[i]     
        newArr[a] = 0
print(newArr)        