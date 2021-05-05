""" Write a function for reversing a linked list.
Your function will have one input: the head of the list.
Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None   """

# Start coding from here


def reverseLinkedList(root):
    cur = root
    prev = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev
