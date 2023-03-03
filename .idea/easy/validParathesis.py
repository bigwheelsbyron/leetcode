def isValid(s) -> bool:
    queueStructure = []
    openingDict = ["(","{","["]
    closingDict = [")","}","]"]
    pairDict = {")":"(","}":"{","]":"["}


    for index,char in enumerate(s):
        if char in openingDict:
            queueStructure.append(char)
        else:
            if char in closingDict:
                if (len(queueStructure) == 0):
                    return False
                if pairDict[char] == queueStructure[len(queueStructure)-1]:
                    queueStructure.pop()
                else:
                    return False
    return len(queueStructure) == 0


print(isValid("})"))