"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.tail = None
        removed_item = self.head
        self.head.delete()
        self.head = removed_item.next
        self.length -= 1
        return removed_item.value

    def add_to_tail(self, value):
        if self.tail == None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        if self.tail == None:
            return None
        elif self.tail == self.head:
            self.head = None
        removed_tail = self.tail
        self.tail.delete()
        self.tail = removed_tail.prev
        self.length -= 1
        return removed_tail.value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.add_to_tail(value)
        self.delete(node)

    def delete(self, node):
        deleted_value = node.value
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
            return deleted_value

    def get_max(self):
        if self.head == None:
            return None
        else:
            current_max = self.head.value
            current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            if current_node.value > current_max:
                current_max = current_node.value

        return current_max
