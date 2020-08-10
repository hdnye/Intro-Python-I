# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def mult_2(num):
    return num * 2

x = 5
x = mult_2(x)
print(x)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# Write a function that takes in a list of numbers and multiplies them all by two

def mult_list_2(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * 2


y = [1,2,3,4]
mult_list_2(y)
print(y)       