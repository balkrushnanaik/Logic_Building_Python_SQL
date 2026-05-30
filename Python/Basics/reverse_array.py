import array as arr

nums = arr.array('i',[1,2,4,5,8,9,3,10,15])
# print(type(nums))
sorted_nums = sorted(nums)
# print(sorted_nums)

# for num in sorted_nums:
#     print(num)

print('Array before reverse:{}'.format(sorted_nums))
sorted_nums.reverse()
print('Array after reverse:{}'.format(sorted_nums))



