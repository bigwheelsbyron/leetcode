
def isPalindrome(s: str) -> bool:
    clean = "".join(filter(str.isalnum, s)).lower()
    leftPointer = 0
    rightPointer = len(clean)-1
    while leftPointer < rightPointer:
        if clean[leftPointer] == clean[rightPointer]:
            leftPointer+=1
            rightPointer-=1
        else:
            return False
    return True



print(isPalindrome(s="A man, a plan, a canal: Panama"))