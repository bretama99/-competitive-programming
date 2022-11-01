#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
from collections import Counter, defaultdict

def has_cycle(head):
    cycle = set()
    cur = head
    while cur:
        if cur in cycle:
            return True
        cycle.add(cur)
        cur = cur.next
    return False
    # slow = fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if fast==slow:
    #         return True
    # return False
    # if not head and not head.next:
    #     return 0
    # cur = head
    # counter = defaultdict(int)
    # while cur:
    #     counter[cur.data]+=1
    #     if counter[cur.data]>1:
    #         return 1
    #     cur = cur.next
    # else:
    #     return 0

        
if __name__ == '__main__':
