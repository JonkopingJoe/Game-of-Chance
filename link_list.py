import random

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
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
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    # def __repr__(self):
    #     return "->".join(str(item) for item in self.to_list())

def get_game_scenarios(instances):
    random.shuffle(instances)
    linked_list = LinkedList()
    for instance in instances:
        linked_list.append(instance)
    return linked_list

# Test
print(get_game_scenarios(["scenario1", "scenario2", "scenario3", 'scenario4']).to_list())

