# creating an empty list 
nums = [] 

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 
	nums.append(ele) # adding the element 
	
print(nums) 

max = nums[0]
for mxim in nums:
	if mxim > max:
		max = mxim
print '\nMaximum number among these is',max
