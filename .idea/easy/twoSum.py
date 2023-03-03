def twoSum(nums, target: int):
    dict = {}

    #strategy
    #   get the difference between the target number and the current number [delta]
    #   get if the detla exists in the dictionary
    #   if the number is in the dictionary, get it's index and return the current index plus delta's index
    #   else, add the number and it's index
    #   if, at the end, there is no match, it isn't there

    for num in range(0,(len(nums))):
        delta = target - nums[num]

        if (dict.get(delta) == None):
            dict[nums[num]] = num
        else:
            return[dict[delta],num]




print(twoSum(nums = [2,7,11,15], target = 9))