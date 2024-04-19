import random

# !!!You could only read the function get_game_scenarios for efficiency
# !!!Please import the classes ListNode and LinkedList and functions get_game_scenarios to use them

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
        try:
            self.value = value
            # Initialize next as null
            self.next = next
        except Exception as e:
            print("An error occured while creating a node, please check the input values!", e)

class LinkedList:
    def __init__(self):
        '''
        Initialize the head of the linked list
        '''
        try:
            self.head = None
        except Exception as e:
            print("An error occured. No parameter needed!",e)

    def append(self, value):
        '''
        Create a new node and append it at the end of the linked list

        Args:
        -value: The value of the node to be appended, here it will be the game scenario

        Returns:
        None
        '''
        try:
            new_node = ListNode(value)
            if not self.head:
                self.head = new_node
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        except Exception as e:
            print("An error occured while appending a node, please check the input values!", e)

    def to_list(self):
        '''
        Convert the linked list to a list

        Args:
        None

        Returns:
        -elements: A list of the elements in the linked list
        '''
        try:
            elements = []
            current = self.head
            while current:
                elements.append(current.value)
                current = current.next
            return elements
        except Exception as e:
            print("An error occured while converting the linked list to a list, please check the input values!", e)

def get_game_scenarios(instances_list):
    '''
    Create a linked list of the game scenarios

    Args:
    -instances: A list of the game scenarios

    Returns:
    -linked_list: A linked list of the game scenarios
    '''
    try:
        random.shuffle(instances_list)
        linked_list = LinkedList()
        for instance in instances_list:
            linked_list.append(instance)
        return linked_list
    except Exception as e:
        print("List needed to be passed, please check input.", e)

# Test
print(get_game_scenarios(["scenario1", "scenario2", "scenario3", 'scenario4']).to_list())
