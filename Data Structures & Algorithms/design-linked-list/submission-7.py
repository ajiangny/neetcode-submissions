class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self): #init empty list
        self.head = None
        self.tail = self.head
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        curr = self.head
        currIndex = 0
        while curr is not None:
            if currIndex == index:
                return curr.val
            else:
                currIndex += 1
                curr = curr.next
        

    def addAtHead(self, val: int) -> None:

        newNode = Node(val)

        if self.length == 0:
            self.head = newNode #if empty, node becomes head
            self.tail = self.head
            self.length += 1
        else:
            curr = self.head #go to first head
            newNode.next = curr #point newNode to the current Node head
            self.head = newNode #self.head is now newNode
            self.length += 1
        

    def addAtTail(self, val: int) -> None:
        
        #what if list is empty?
        if self.length == 0:
            self.addAtHead(val)
            return

        newNode = Node(val)
        
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        #if index is 0, just add to head
        if index == 0: 
            self.addAtHead(val)
            return
        #if index is equal to the length, add to tail
        if index == self.length:
            self.addAtTail(val)
            return

        newNode = Node(val)
        currIndex = 1
        prev = self.head
        curr = self.head.next

        while currIndex != index:
            prev = prev.next
            curr = curr.next
            currIndex += 1

        prev.next = newNode
        newNode.next = curr
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        currIndex = 1
        prev = self.head
        curr = self.head.next

        while currIndex != index:
            prev = prev.next
            curr = curr.next
            currIndex += 1

        if currIndex == self.length - 1:
            prev.next = None
            self.tail = prev
            self.length -= 1
            return
        
        prev.next = curr.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)