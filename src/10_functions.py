# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False   

x = 5
x = is_even(x)
print(x)

 

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
#num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = 0
# odds = 0

# for num in num_list:
#     if num % 2 == 0:
#         evens += 1
#     else: 
#         odds += 1     

if num % 2:
    print('This is an odd number')   
else:
    print('This is an even number')
        


# Write a function that takes in a list of numbers and multiplies them all by two

def mult_list_2(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * 2

y = [1,2,3,4]
mult_list_2(y)
print(y)       
