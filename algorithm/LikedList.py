# class Node
# class LinkedList:
#   __init__      → head, tail 둘 다 None
#   push_front    → tail도 챙기기 (빈 리스트일 때)
#   push_back     → 위 코드
#   pop_front     → 비면 tail도 None으로
#   print_all

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

    def push_back(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop empty list")
        
        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        return value
    
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next