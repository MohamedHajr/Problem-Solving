def twoSum(nums, target):
    sums = dict()
    result = []

    for i, number in enumerate(nums):
        diff = target - number 
        print(diff)
        if diff in sums:
            result.append(sums[diff])
            result.append(i)
        sums[number] = i
        
    return result 

print(twoSum([-3, 4, 3, 90], 0))
