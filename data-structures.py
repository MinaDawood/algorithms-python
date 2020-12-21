# Arrays

# Linked Lists
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count += 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# itemList = LinkedList()
# itemList.insert(1)
# itemList.insert(2)
# itemList.insert(3)
# itemList.insert(4)
# itemList.dump_list()

# print("Item count: ", itemList.get_count())
# print("Finding item: ", itemList.find(4))
# print("Finding item: ", itemList.find(6))

# itemList.deleteAt(3)
# print("Item count: ", itemList.get_count())
# print("Finding item: ", itemList.find(3))
# itemList.dump_list()

####################################################################################################
# Stacks and Queues

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

x = stack.pop()
print(x)
print(stack)

# Queue
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

x = queue.popleft()
print(x)
print(queue)

####################################################################################################
# Hash Tables
items1 = dict({"key1" : 1,"key2" : 2,"key3" : 3,})