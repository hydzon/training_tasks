"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

"""


class Node:

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return str(self.val)


def printList(p_node):
    while p_node:
        print(p_node.val)
        p_node = p_node.next_node


def GetMiddleNode(head, i):
    if head == None:
        return i // 2
    x = GetMiddleNode(head.next_node, i + 1)
    if i == x:
        return head
        pass
    else:
        return x


n = int(input())
head = Node(1)
p = head
for i in range(1, n):
    p.next_node = Node(i + 1)
    p = p.next_node

#printList(head)
print(GetMiddleNode(head, 1))
