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
    "Yay! That stray cat that always gouges your eyes out is nowhere in sight!",
    "OW! That cat is here today, you just got scratched ;(",
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
    "You run and catch the bus just in time. The driver smiles and nods as you hop on, finding a surprisingly good seat. ",
    "You sprint, but just as you reach the door, the bus pulls away. Now you're sweaty and still need to wait for the next one.",
    # Second
    "Wait for the next bus",
    "The next bus arrives quickly, and it's much less crowded than usual. You get a whole seat to yourself.",
    "The next bus is delayed, and you're late for work, adding stress to your morning.",
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


# Scenario 2: Networking Event Invitation
scenario9 = Scenario("path/to/picture.jpg")
scenario9.set_cases(
    "You receive a last-minute invitation to a networking event. Do you attend or decline to have a quiet evening at home?",
    "Attend the event.",
    "You make valuable contacts that could benefit your career.",
    "The event is dull, and you regret not spending the evening relaxing.",
    "Decline and stay home.",
    "You enjoy a restful evening that prepares you for tomorrow.",
    "You hear later about missed opportunities from the event."
)

# Scenario 3: Evening Jog
scenario10 = Scenario("path/to/picture.jpg")
scenario10.set_cases(
    "Feeling energetic, you consider going for an evening jog. Do you hit the park or the gym treadmill?",
    "Jog in the park.",
    "The fresh air invigorates you, boosting your mood.",
    "It starts raining heavily, cutting your jog short.",
    "Use the gym treadmill.",
    "You have a productive workout session and feel great.",
    "The gym is overcrowded, and you barely get any time on the treadmill."
)

# Scenario 5: Grocery Shopping
scenario11 = Scenario("path/to/picture.jpg")
scenario11.set_cases(
    "You realize you need groceries. Do you stop by the store on your way home or order delivery?",
    "Visit the grocery store.",
    "You find everything you need on sale.",
    "The store is crowded, and shopping takes longer than expected.",
    "Order groceries for delivery.",
    "The delivery is quick and saves you time.",
    "The delivery is late and missing items."
)

# Scenario 6: Dinner Options
scenario12 = Scenario("path/to/picture.jpg")
scenario12.set_cases(
    "It's time for dinner, but you're not in the mood to cook. Do you order in or go out to eat?",
    "Order in.",
    "The food arrives quickly and tastes delicious.",
    "The order is wrong and arrives late.",
    "Go out to eat.",
    "You enjoy a great meal out and feel content.",
    "The restaurant is full, and you end up waiting a long time."
)

# Scenario 7: Relaxing Activities
scenario13 = Scenario("path/to/picture.jpg")
scenario13.set_cases(
    "You feel the need to unwind. Do you read a book or watch a movie?",
    "Read a book.",
    "You get completely absorbed in an amazing story.",
    "You find it hard to focus and don’t enjoy the book.",
    "Watch a movie.",
    "You watch a fantastic movie that you thoroughly enjoy.",
    "The movie is disappointing, and you regret not choosing another activity."
)

# Scenario 8: Online Coursework
scenario14 = Scenario("path/to/picture.jpg")
scenario14.set_cases(
    "You remember you’ve signed up for an online course. Do you catch up on lessons tonight or decide to postpone?",
    "Catch up on the course.",
    "The coursework is engaging, and you feel productive.",
    "You’re too tired to absorb the information, wasting your time.",
    "Postpone to another day.",
    "You take the evening off, which proves to be the right choice.",
    "You fall behind and stress about catching up later."
)

# Scenario 9: Evening Class
scenario15 = Scenario("path/to/picture.jpg")
scenario15.set_cases(
    "You have the option to attend a local evening class. Do you go for a yoga class to relax or a cooking class to improve your culinary skills?",
    "Attend yoga class.",
    "The yoga session is rejuvenating, and you leave feeling refreshed and centered.",
    "The class is overbooked, and you find it hard to relax in the crowded room.",
    "Attend cooking class.",
    "You learn a new recipe that becomes a new favorite at home.",
    "The class moves at a fast pace, and you struggle to keep up."
)

# Scenario 11: Social Media Detox
scenario16 = Scenario("path/to/picture.jpg")
scenario16.set_cases(
    "You consider taking a break from social media for the evening. Do you follow through with a detox, or end up scrolling through feeds?",
    "Complete the detox.",
    "The break from screens improves your sleep and mental clarity.",
    "You feel out of the loop and a bit isolated.",
    "Scroll through social media.",
    "You catch up on news and engage with friends, feeling connected.",
    "You spend too much time online and go to bed late, feeling drained."
)




# Scenarios Tree
root = TreeNode(scenario1)

# Second Level 
second_left_branch = TreeNode(scenario2)
second_right_branch = TreeNode(scenario3)  

# Third Level 
third_left_branch_left = TreeNode(scenario4)
third_left_branch_right = TreeNode(scenario5)

third_rigth_branch_left = TreeNode(scenario6)
third_right_branch_right = TreeNode(scenario7)

# Fourth Level 
third_left_branch_left.left = scenario8
third_left_branch_left.right= scenario9

third_left_branch_right.left = (scenario9)
third_left_branch_right.right = (scenario10)



third_rigth_branch_left.left = (scenario11)
third_rigth_branch_left.right = (scenario12)


third_right_branch_right.left = (scenario13)
third_right_branch_right.left= (scenario14)


# TREE SECTION
second_left_branch.left = (third_left_branch_left)
second_left_branch.right = (third_left_branch_right)


second_right_branch.left = (third_rigth_branch_left)
second_right_branch.right = (third_right_branch_right)


# # Main Tree
root.left = (second_left_branch)
root.right = (second_right_branch)



def my_inorder(root_node): 
    current = root_node 
    if type(current) == None: 
        return 
    my_inorder(current.left)
    print(current.data)
    my_inorder(current.right)



my_inorder(root)










