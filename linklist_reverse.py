class node:
    def __init__(self, data= None, next=None) -> None:
        self.data = data
        self.next = next

class linked_list:
    def __init__(self) -> None:
        self.head = None

    def forward_ll(self, data):
        new_node = node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    

    def reverse_ll(self):
        if self.head is None:
            return 
        if self.head.next is None:
            return    
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        # return self.head
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next    
        print("NULL")

ll = linked_list()
ll.forward_ll(1)
ll.forward_ll(2)
ll.forward_ll(3)
ll.forward_ll(4)
ll.forward_ll(5)
ll.forward_ll(67)
ll.forward_ll(78)
ll.forward_ll(89)
ll.forward_ll(90)
ll.forward_ll(100)
print("Original Linked List")
ll.display()
print('Reversed Linked List')
ll.reverse_ll()
ll.display()
