# Alex Bello
# 3/3/2020
# ADV PROG TECH


class New_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

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

    def add_to_end(self, data):
        if not self.head:
            self.head = New_Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = New_Node(data=data, prev=curr)

    def remove_from_head(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def remove_from_end(self, node):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        if self.next=None:
            New_Node.head = None
            New_Node.prev = self.data



