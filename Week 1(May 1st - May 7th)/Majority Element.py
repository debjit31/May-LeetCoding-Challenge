# Majority Element
# Solution
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


from collections import defaultdict
nums = list(map(int, input().split(',')))
max_count = len(nums) // 2
count = defaultdict()
for i in nums:
	count[i] = 0
for i in nums:
	count[i] += 1
	if count[i] > max_count:
		print(i)
		break
print(count)

