import random

class ListNode:
    # Constructor to initialize the node object
    def __init__(self, value, next=None):
        '''
        Assign data to a node. In our project it will be the game scenario

        Args: 
        -value: The value of the node
        -next: The next node in the linked list

        Returns:
        None
        '''
        self.value = value
        # Initialize next as null
        self.next = next

class LinkedList:
    def __init__(self):
        '''
        Initialize the head of the linked list
        '''
        self.head = None

    def append(self, value):
        '''
        Create a new node and append it at the end of the linked list

        Args:
        -value: The value of the node to be appended, here it will be the game scenario

        Returns:
        None
        '''
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # def insert_at_beginning(self, value):
    #     new_node = ListNode(value, self.head)
    #     self.head = new_node

    def to_list(self):
        '''
        Convert the linked list to a list

        Args:
        None

        Returns:
        -elements: A list of the elements in the linked list
        '''
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    # def __repr__(self):
    #     return "->".join(str(item) for item in self.to_list())

def get_game_scenarios(instances_list):
    '''
    Create a linked list of the game scenarios

    Args:
    -instances: A list of the game scenarios

    Returns:
    -linked_list: A linked list of the game scenarios
    '''
    random.shuffle(instances_list)
    linked_list = LinkedList()
    for instance in instances_list:
        linked_list.append(instance)
    return linked_list

# Test
print(get_game_scenarios(["scenario1", "scenario2", "scenario3", 'scenario4']).to_list())

