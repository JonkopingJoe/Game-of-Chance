# Create a Linkedlist_node class to create a Linkedlist_node
class Linkedlist_node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a Linkedlist_node at begin of LL
    def insertAtBegin(self, data):
        new_linkedlist_node = Linkedlist_node(data)
        if self.head is None:
            self.head = new_linkedlist_node
            return
        else:
            new_linkedlist_node.next = self.head
            self.head = new_linkedlist_node

    # Method to add a Linkedlist_node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_linkedlist_node = Linkedlist_node(data)
        current_Linkedlist_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_Linkedlist_node != None and position+1 != index):
                position = position+1
                current_Linkedlist_node = current_Linkedlist_node.next

            if current_Linkedlist_node != None:
                new_linkedlist_node.next = current_Linkedlist_node.next
                current_Linkedlist_node.next = new_linkedlist_node
            else:
                print("Index not present")

    # Method to add a Linkedlist_node at the end of LL

    def insertAtEnd(self, data):
        new_linkedlist_node = Linkedlist_node(data)
        if self.head is None:
            self.head = new_linkedlist_node
            return

        current_Linkedlist_node = self.head
        while(current_Linkedlist_node.next):
            current_Linkedlist_node = current_Linkedlist_node.next

        current_Linkedlist_node.next = new_linkedlist_node

    # Update Linkedlist_node of a linked list
        # at given position
    def updateLinkedlist_node(self, val, index):
        current_Linkedlist_node = self.head
        position = 0
        if position == index:
            current_Linkedlist_node.data = val
        else:
            while(current_Linkedlist_node != None and position != index):
                position = position+1
                current_Linkedlist_node = current_Linkedlist_node.next

            if current_Linkedlist_node != None:
                current_Linkedlist_node.data = val
            else:
                print("Index not present")

    # Method to remove first Linkedlist_node of linked list

    def remove_first_Linkedlist_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Method to remove last Linkedlist_node of linked list
    def remove_last_Linkedlist_node(self):

        if self.head is None:
            return

        current_Linkedlist_node = self.head
        while(current_Linkedlist_node.next.next):
            current_Linkedlist_node = current_Linkedlist_node.next

        current_Linkedlist_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_Linkedlist_node = self.head
        position = 0
        if position == index:
            self.remove_first_Linkedlist_node()
        else:
            while(current_Linkedlist_node != None and position+1 != index):
                position = position+1
                current_Linkedlist_node = current_Linkedlist_node.next

            if current_Linkedlist_node != None:
                current_Linkedlist_node.next = current_Linkedlist_node.next.next
            else:
                print("Index not present")

    # Method to remove a Linkedlist_node from linked list
    def remove_Linkedlist_node(self, data):
        current_Linkedlist_node = self.head

        if current_Linkedlist_node.data == data:
            self.remove_first_Linkedlist_node()
            return

        while(current_Linkedlist_node != None and current_Linkedlist_node.next.data != data):
            current_Linkedlist_node = current_Linkedlist_node.next

        if current_Linkedlist_node == None:
            return
        else:
            current_Linkedlist_node.next = current_Linkedlist_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_Linkedlist_node = self.head
            while(current_Linkedlist_node):
                size = size+1
                current_Linkedlist_node = current_Linkedlist_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_Linkedlist_node = self.head
        while(current_Linkedlist_node):
            print(current_Linkedlist_node.data)
            current_Linkedlist_node = current_Linkedlist_node.next


# create a new linked list
llist = LinkedList()

# add Linkedlist_nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Linkedlist_node Data")
llist.printLL()

# remove a Linkedlist_nodes from the linked list
print("\nRemove First Linkedlist_node")
llist.remove_first_Linkedlist_node()
print("Remove Last Linkedlist_node")
llist.remove_last_Linkedlist_node()
print("Remove Linkedlist_node at Index 1")
llist.remove_at_index(1)


# print the linked list again
print("\nLinked list after removing a Linkedlist_node:")
llist.printLL()

print("\nUpdate Linkedlist_node Value")
llist.updateLinkedlist_node('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())
