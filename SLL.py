# Linked List

# Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked List class
class SLL:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def insertBeginnig(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            firstNode = newNode
            firstNode.next = self.head
            self.head = firstNode
    
    def printList(self):
        if self.head is None:
            print("The list is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                print(None)
                break
            print(currentNode.data, end=' -> ')
            currentNode = currentNode.next

# Creating a node
firstNode = Node("Harsh")
linkedList = SLL()
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Mathew")
linkedList.insertEnd(thirdNode)
fourthNode = Node("Anna")
linkedList.insertBeginnig(fourthNode)
linkedList.printList()