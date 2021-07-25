# Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class SLL:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                #if lastNode.next is None:
                #    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
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
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Mathew")
linkedList.insert(thirdNode)
linkedList.printList()