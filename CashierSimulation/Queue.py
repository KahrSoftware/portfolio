'''
CSCI 204 Lab 08 Priority Queue ADT
Lab section: CSCI 204.L61, Thursday 1:00-2:52
Student name: Justin Kahr
Instructor name: Professor Scherr
'''

class Node:
    """Node in the list. Has data and stores reference to next node."""
    def __init__(self, data):
        self.data = data
        self.next = None        

class Queue:
    """Implements a first in last out queue adt"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """Return the sie of our queue"""
        return self.size

    def is_empty(self):
        """Check if size is equal to zero"""
        return self.size == 0

    def dequeue(self):
        """Take out the first item from the queue and return it"""        
        assert not self.is_empty(), "Cannot Dequeue From Empty Queue"
        out = self.head.data
        self.head = self.head.next
        self.size -= 1
        return out
    
    def enqueue(self, data):
        """Add some data to a node, and put it at the end of the queue"""        
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
