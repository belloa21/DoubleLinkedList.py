# Alex Bello
# 3/3/2020
# ADV PROG TECH


class New_Node:
    def __init__(self, data=none, prev=none, next=none):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = none

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def add_to_head(self, data):
        new_head = New_Node(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head
