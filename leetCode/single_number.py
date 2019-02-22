# class Solution:
#     def singleNumber(self, nums: 'List[int]') -> 'int':
#         hashset = set()
#         for num in nums:
#             if num in hashset:
#                 hashset.remove(num)
#             else:
#                 hashset.add(num)
#         return hashset.pop()
from functools import reduce

def singleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums)

print(singleNumber([1,2,2,3,3]))