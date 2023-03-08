def replaceElements(arr):
    returnArray = []
    for i in range(0,len(arr)):
        nextIndex = i+1
        subArray = arr[nextIndex:]

        if len(subArray) != 0:
            highest = max(subArray)
            returnArray.append(highest)
        else:
            returnArray.append(-1)

    return returnArray

