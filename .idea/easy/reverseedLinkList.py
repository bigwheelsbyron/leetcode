
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    returnArray = []
    array = []
    currentNode = head
    while True:
        nextNode = currentNode.next
        if(nextNode != None):
            array.append(nextNode)
            currentNode = nextNode
        else:
            break
    for i in range(0,len(array)):
        returnArray.append(array[-(i+1)])
    print(array)
    print(returnArray)

lList = []
for i in range(0,4):
    if(len(lList)==0):
        x = ListNode(1)
        lList.append(x)
    else:
        x = ListNode(val=i+1,next=lList[len(lList)-1])
        lList.append(x)

reverseList(lList[len(lList)-1])