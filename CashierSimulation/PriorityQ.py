'''
CSCI 204 Lab 08 Priority Queue ADT
Lab section: CSCI 204.L61, Thursday 1:00-2:52
Student name: Justin Kahr
Instructor name: Professor Scherr
'''

from Queue import Queue
from Queue import Node

class PriorityQueue( Queue ):
    """Implements a priority queue adt"""

    def __init__( self, ):
        """Initialize the queue with a default number of priority classes."""
        super().__init__()

    def __str__( self ):
        """Return the name of the queue"""
        return "PriorityQueue"

    def enqueue( self, priority, item ):
        """Insert an item with priority at the right place."""
        # Overriding of enqueue from Queue 
        node = PNode(item, priority)
        if self.head == None or self.head.priority > node.priority:
            node.next = self.head
            self.head = node
            self.size += 1
            return
        test = self.head
        while (not test.next == None) and test.next.priority <= node.priority:
            test = test.next
        node.next = test.next
        test.next = node
        self.size += 1

    # Use the dequeue method inherited from Queue

class PNode( Node ):
    """Implements nodes with a priority using node inherited from Queue."""
    def __init__(self, data, priority):
        self.priority = priority
        super().__init__(data)
