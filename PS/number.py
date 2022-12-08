'''
// means After divide take floor number value
%  means take the remainder value

'''
# def allNum(num):
#     print('Given Num', num)
#     while num > 9:
#         sum = 0
#         while num:
#             print('Take the last number =>', num%10)
#             sum += num%10
#             print('Remove the last number =>', num//10)
#             num = num//10
#         print('updated sum', sum)    
#         num = sum
#     return num 

# print("TOtal Count =>",allNum(346))

# def addDigits(num):
#     if num == 0 : return 0
#     if num % 9 == 0 : return 9
#     else :return(num % 9)
# print("Total Count =>",addDigits(346))

def removeElement(nums, val):
        # nums is null then return - 0
        if len(nums) == 0:
            return 0
        
        #take a variable that will return the counter length
        k = 0
        
        #look through the whole nums and find out the value
        
        for i in range(len(nums)):
            #check if the nums values are mathches with the val
            #if match then skip
            #else increase k and swaped value 
            
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k     

print(removeElement([3,3,2,1,0], 2))