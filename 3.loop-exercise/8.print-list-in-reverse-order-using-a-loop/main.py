def reverseArr(arr):
    res = arr[::-1]
    print(res)
    return res

reverseArr([10, 20, 30, 40, 50])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        if self.next is None:
            return f"{{value: {self.value}, next: None}}"
        else:
            return f"{{value: {self.value}, next: {str(self.next)}}}"
class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = self.head

    def __str__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.value))
            current = current.next
        return "[" + " -> ".join(nodes) + "]"
    def add(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode

ll = LinkedList(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)

print('init linkedList: ',ll)
def reverseLinkedList(list:LinkedList):
    prev = None
    curr = list.head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    list.head = prev
    print(list)
    return

reverseLinkedList(ll)