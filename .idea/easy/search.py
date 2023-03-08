def search(nums, target) -> int:
    leftPointer = 0
    rightPointer = len(nums)-1
    while leftPointer <= rightPointer:
        middle = (leftPointer + rightPointer) //2
        if (nums[middle] > target):
            rightPointer = middle-1
        elif (target > nums[middle]):
            leftPointer = middle+1
        elif (target == nums[middle]):
            return middle
    return -1


print(search(nums = [-1,0,3,5,9,12], target = 13))