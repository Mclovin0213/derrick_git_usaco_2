class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newData):
        newNode = Node(newData)

        if self.head == None:
            self.head = newNode
            return

        last = self.head
        while last.next != None:
            last = last.next

        last.next = newNode
    
    def push(self, newData):
        newNode = Node(newData)
        
        newNode.next = self.head

        self.head = newNode

    def delete(self, key):
        prev = None

        if self.head == None:
            return
        
        temp = self.head

        if temp.data == key:
            self.head = tenp.next
            temp = None
            return

        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None