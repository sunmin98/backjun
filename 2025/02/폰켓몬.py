def solution(nums):
	length = len(nums) //2
	# print(length)
	set_list =len(set(nums))
	# print(set_list)

	if length < set_list: return print(length)
	else: print(len(set(nums)))

nums =[]
nums = [3, 1, 2, 3]
# nums = [3, 3, 3, 2, 2, 4]
# nums = [3, 3, 3, 2, 2, 2]

solution(nums)