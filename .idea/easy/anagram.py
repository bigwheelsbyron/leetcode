def isAnagram(s: str, t: str) -> bool:
    sDict = {}
    tDict = {}

    if(len(s) != len(t)):
        return False

    for i in s:
        if sDict.get(i) == None:
            sDict[i] = 1
        else:
            sDict[i] += 1

    for i in t:
        if tDict.get(i) == None:
            tDict[i] = 1
        else:
            tDict[i] += 1

    for key in sDict.keys():
        if (sDict.get(key) != tDict.get(key)):
            return False
        else:
            continue
    return True

print(isAnagram(s="catdoog",t="dogcat")) #false
print(isAnagram(s="catdog",t="dogcat")) #true
print(isAnagram(s="catdoog",t="dorcat")) #false