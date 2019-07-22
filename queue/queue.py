class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we use to store queue elements?
        self.storage = Linked_List()

    def enqueue(self, item):
        self.storage.add_tail(item)  # adding an item to the end of the list
        self.size += 1  # incrementing by 1

    def dequeue(self):
        dequeued = None
        if self.storage.head != None:  # if the item in the list at the beginning is not none
            dequeued = self.storage.head.value  # dequeued is the value of that item
            self.storage.del_head()  # then delete that item
            self.size -= 1  # make the list 1 size smaller
            return dequeued

    def len(self):
        return self.size  # return the size


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_value(self, new_value):
        self.value = new_value


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, value):
        new_head = Node(value, self.head)
        if self.head == None:  # if there is no beginning item
            self.tail = new_head  # the tail becomes the head
        self.head = new_head  # added item goes to the front

    def del_head(self):
        if self.head.get_next() == None:  # if the item after the first item is not there
            self.tail = None  # there is no end item
        # but if it is there get the next one, which skips or deletes the first one
        self.head = self.head.get_next()

    def add_tail(self, value):
        if self.tail == None:  # if the last item isnt there
            self.add_head(value)  # show the first and only item in the list
        else:  # OtHeRwIsE
            # make new_tail be the next node value added in(which will be at the end)
            new_tail = Node(value)
            self.tail.set_next(new_tail)
            self.tail = new_tail

    def del_tail(self):
      # if current.get_next is nothing then set the first and the last to none
      # meaning it deletes everything in there.
        current = self.head
        if current.get_next() == None:
            self.head = None
            self.tail = None
        while current.get_next() == self.tail:
          # while the next item in the list is the last item in the list
            current = current.get_next()
        self.tail = current
        # current is the last item in the list
        self.tail.set_next(None)
        # set the next item in the list to none. meaning it gets deleted.
