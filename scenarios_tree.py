from scenario import Scenario


# Helper Class that allocates a new TreeNode 
# with the given data and None left and 
# right pointers. 
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None

def hasPath(root: TreeNode, child_value: Scenario, arr):
    if not root:
        return False
        
    arr.append(root.data)	 

    if root.data == child_value:	 
        return True
    
    if hasPath(root.left, child_value, arr) or hasPath(root.right, child_value, arr): 
        return True
     
    arr.pop(-1) 
    return False

# function to print the path from root to 
# the given TreeNode if the TreeNode lies in
# the binary tree 
def getPath(root, child_value) -> list:
    result_list = []
    
    # vector to store the path 
    arr = [] 

    
    # if required TreeNode 'child_value' is present 
    # then print the path 
    if (hasPath(root, child_value, arr)):
        for i in range(len(arr) - 1):
            result_list.append(arr[i]) 
        result_list.append(arr[len(arr) - 1])
    
    # 'child_value' is not present in the 
    # binary tree 

    return result_list


# ROOT (FIRST LAYER)
scenario1 = Scenario("./waittrain_late_small.jpg")
scenario1.set_cases(
    """The Day Begins.
    Let's get you to work! 
    Which door are you leaving your house through?""",

    # First
    "Front Door", 
    f"Yay! That stray cat that always gouges your eyes out is nowhere in sight!",
    f"OW! That cat is here today, you just got scratched ;(",
    # Second
    "The Back Door",
    f"Phew, narrowly escaped that nosy neighbour!",
    f"Oh no, you tripped over that bucket of water you left out last night!"
    )


# SECOND LAYER
scenario2 = Scenario("Graphics/scenario1_leave_house.png")
scenario2.set_cases(
    "As you approach the bus stop, you see your bus is already there, about to leave. What do you do?",
    # First
    "Run to catch the bus",
    f"You run and catch the bus just in time. The driver smiles and nods as you hop on, finding a surprisingly good seat. ",
    f"You sprint, but just as you reach the door, the bus pulls away. Now you're sweaty and still need to wait for the next one.",
    # Second
    "Wait for the next bus",
    f"The next bus arrives quickly, and it's much less crowded than usual. You get a whole seat to yourself.",
    f"The next bus is delayed, and you're late for work, adding stress to your morning.",
)


scenario3 = Scenario("./waittrain_late_small.jpg")
scenario3.set_cases(
    "As you walk to work, it starts to rain unexpectedly. Do you seek immediate shelter or power through to work?",
    # First
    "Seek shelter.",
    "While taking shelter, you bump into a colleague and have a great conversation that leads to a new work collaboration",
    "The rain gets heavier, and you end up getting soaked anyway, as the shelter isn't very effective.",
    # Second
    "Power through to work",
    "The rain stops as quickly as it started, and you arrive at work slightly damp but on time.",
    "You arrive drenched, and it's uncomfortable until your clothes dry, affecting your focus.",
)

# THIRD LAYER
scenario4 = Scenario("./waittrain_late_small.jpg")
scenario4.set_cases(
    "after you arrive to work, You receive an urgent email from a client requesting immediate  changes to a project. Do will you do?",
    # First
    "Prioritize the client's request.",
    "Your quick response impresses the client, leading to potential new opportunities",
    "You miss a crucial detail in your rush, leading to further complications.",
    # Second
    "Stick to your planned tasks.",
    "By sticking to your plans, you finish another important task flawlessly",
    "The client is upset with the delay, causing tension in the relationship.",
)


scenario5 = Scenario("./waittrain_late_small.jpg")
scenario5.set_cases(
    "You receive a last-minute request to join an additional meeting, but you're already swamped with work. Do you attend the meeting or decline?",
    # First
    "Attend the meeting",
    "The meeting turns out to be crucial, and your input is highly valued.",
    "The meeting is unproductive, and you fall behind on your work",
    # Second
    "Decline the meeting",
    "You make significant progress on your projects by declining. ",
    "You miss out on important information shared in the meeting.",
)


scenario6 = Scenario("./waittrain_late_small.jpg")
scenario6.set_cases(
    "A client decides to visit the office unexpectedly. Do you volunteer to greet and handle the client, or do you let your colleagues manage?",
    # First
    "Greet the client.",
    "The client is impressed with your initiative and professionalism.",
    "You get caught up with the client longer than expected, disrupting your schedule.",
    # Second
    "Let colleagues handle it.",
    "Your colleagues handle the situation well, and you focus on your tasks.",
    "The client needed information only you could provide, leading to a missed opportunity.",
)



scenario7 = Scenario("path/to/picture.jpg")
scenario7.set_cases(
    "Your office conducts an unexpected fire safety drill. Do you take it seriously or use it as a chance to catch up outside with colleagues?",
    # First
    "Take it seriously.",
    "You learn valuable safety information.",
    "The drill is longer than expected, eating into your work time.",
    # Second
    "Casual catch-up.",
    "You strengthen bonds with your colleagues, improving teamwork.",
    "You miss some critical safety instructions."
)



scenario8 = Scenario("path/to/picture.jpg")
scenario8.set_cases(
    "You're offered an unexpected project that is challenging but could be a big career boost. Do you accept the challenge or decline due to your current workload?",
    # First
    "Accept the project.",
    "The project leads to significant professional growth and recognition.",
    "The project overwhelms you, impacting your performance on other tasks.",
    # Second 
    "Decline the project.",
    "You maintain a manageable workload, ensuring all tasks are done well.",
    "You miss out on a potential career-defining opportunity."
)


# FORTH LAYER














