from random import choice
from scenario import Scenario
from linkedlist import Linkedlist

# Helper Class that allocates a new TreeNode 
# with the given data and None left and 
# right pointers. 
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

def hasPath(root: TreeNode, child_value: Scenario, arr: list) -> bool:
    if not root:
        return False
        
    arr.append(root.data)	 

    if root.data == child_value:	 
        return True
    
    if hasPath(root.left, child_value, arr) or hasPath(root.right, child_value, arr): 
        return True
     
    arr.pop(-1) 
    return False


def getPath(root, child_value) -> Linkedlist:
    result_linkedlist = Linkedlist()
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


    for i in result_list: 
        result_linkedlist.insertAtEnd(i)

    return result_linkedlist



def get_game_scenarios() -> Linkedlist: 
    last_layer_nodes = [
        scenario8, 
        scenario9, 
        scenario10, 
        scenario11, 
        scenario12, 
        scenario13, 
        scenario14,
        scenario15, 
    ]


    random_scenario = choice(last_layer_nodes)
    return getPath(root, random_scenario)



# ROOT (FIRST LAYER)
scenario1 = Scenario("Graphics/back_door_safe.png")
scenario1.set_cases(
    "The Day Begins. Let's get you to work! Which door are you leaving your house through?",

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
scenario2 = Scenario("Graphics/puddle_fail.png")
scenario2.set_cases(
    "While on your way to the train station,"
    "\nyou see a big puddle on the road, what do you do?",
    "Jump over it",
    f"Way to go!\nThose long jumps during physical education coming in clutch!",
    f"Leg days? 404 not found.\nwhat made you think you could do it?",
    "Walk gently",
    f"Phew! You made it, slowly but surely.",
    f"Nuh uh those converse wont hold,\nyour feet are taking a bath."
    )

scenario3 = Scenario("Graphics/phone_notif.png")
scenario3.set_cases(
    "Ding! Would you like to buy the lottery?",
    "Yes!",
    f"Oh my! You won some money!",
    f"Uh oh, that was a scam website :o",
    "Nah",
    f"Good job for not getting scammed, you won a prize!",
    f"You missed they giveaway they were doing"
    f"\nfor everyone who bought lottery :("
    )

# THIRD LAYER
scenario4 = Scenario("Graphics/wait_for_train.png")
scenario4.set_cases(
    "At the train station,"
    "\nyou just bought coffee, oh no! that train is here!",
    "Wait for next train",
    f"The next train came early!"
    f"\nYou enjoyed your coffee and got to work on time.",
    f"the train was terminated :|",
    "RUN!!",
    f"You caught the train! Off to work we go!",
    f"You caught the train, but at what cost..."
    f"\nYou are now drenched in coffee."
    )

scenario5 = Scenario("Graphics/unexpected_project.png")
scenario5.set_cases(
    "You're offered an unexpected project that is challenging "
    "\nbut could be a big career boost. What will you do?",
    # First
    "Accept the project.",
    "The project leads to significant professional growth and recognition.",
    "The project overwhelms you, impacting your performance on other tasks.",
    # Second
    "Decline the project.",
    "You maintain a manageable workload, ensuring all tasks are done well.",
    "You miss out on a potential career-defining opportunity."
)

scenario6 = Scenario("Graphics/unexpected_client.png")
scenario6.set_cases(
    "A client decides to visit the office unexpectedly. What will you do?",
    # First
    "Greet the client.",
    "The client is impressed with your initiative and professionalism.",
    "You get caught up with the client longer than expected, disrupting your schedule.",
    # Second
    "Let colleagues handle it.",
    "Your colleagues handle the situation well, and you focus on your tasks.",
    "The client needed information only you could provide, leading to a missed opportunity.",
)

scenario7 = Scenario('Graphics/fire_drill.png')
scenario7.set_cases(
    "Your office conducts an unexpected fire safety drill. "
    "\nDo you take it seriously or use it as a chance to catch up outside with colleagues?",
    # First
    "Take it seriously.",
    "You learn valuable safety information.",
    "The drill is longer than expected, eating into your work time.",
    # Second
    "Casual catch-up.",
    "You strengthen bonds with your colleagues, improving teamwork.",
    "You miss some critical safety instructions."
)

scenario8 = Scenario("Graphics/networking_event.png")
scenario8.set_cases(
    "You receive a last-minute invitation to a networking event."
    "\nDo you attend or decline to have a quiet evening at home?",
    "Attend the event.",
    "You make valuable contacts that could benefit your career.",
    "The event is dull, and you regret not spending the evening relaxing.",
    "Decline and stay home.",
    "You enjoy a restful evening that prepares you for tomorrow.",
    "You hear later about missed opportunities from the event.")

# FORTH LAYER
scenario9 = Scenario("Graphics/meeting.png")
scenario9.set_cases(
    "You receive a last-minute request to join an additional meeting,"
    "\nbut you're already swamped with work. Do you attend the meeting or decline?",
    "Attend",
    "The meeting turns out to be crucial, and your input is highly valued.",
    "The meeting is unproductive, and you fall behind on your work :(",
    "Decline",
    "You made significant progress on your projects by declining. ",
    "You missed out on important information shared in the meeting!!")


# Scenario 3: Evening Jog
scenario10 = Scenario("Graphics/exercise.png")
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
scenario11 = Scenario("Graphics/grocery.png")
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
scenario12 = Scenario("Graphics/dinner.png")
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
scenario13 = Scenario("Graphics/relax.png")
scenario13.set_cases(
    "You feel the need to unwind. Do you read a book or watch a movie?",
    "Read a book.",
    "You get completely absorbed in an amazing story.",
    "You find it hard to focus and don't enjoy the book.",
    "Watch a movie.",
    "You watch a fantastic movie that you thoroughly enjoy.",
    "The movie is disappointing, and you regret not choosing another activity."
)

# Scenario 8: Online Coursework
scenario14 = Scenario("Graphics/online_class.png")
scenario14.set_cases(
    "You remember you've signed up for an online course. Do you catch up on lessons tonight or decide to postpone?",
    "Catch up on the course.",
    "The coursework is engaging, and you feel productive.",
    "You're too tired to absorb the information, wasting your time.",
    "Postpone to another day.",
    "You take the evening off, which proves to be the right choice.",
    "You fall behind and stress about catching up later."
)

# Scenario 9: Evening Class
scenario15 = Scenario("Graphics/local_class.png")
scenario15.set_cases(
    "You have the option to attend a local evening class. Which will you choose?",
    "Attend yoga class.",
    "The yoga session is rejuvenating, and you leave feeling refreshed and centered.",
    "The class is overbooked, and you find it hard to relax in the crowded room.",
    "Attend cooking class.",
    "You learn a new recipe that becomes a new favorite at home.",
    "The class moves at a fast pace, and you struggle to keep up."
)


# Scenarios Tree
root = TreeNode(scenario1)


# Second Level 
node2 = TreeNode(scenario2)
node3 = TreeNode(scenario3)  

# Third Level 
node4 = TreeNode(scenario4)
node5 = TreeNode(scenario5)

node6 = TreeNode(scenario6)
node7 = TreeNode(scenario7)

# Fourth Level 
node4.left = TreeNode(scenario8)
node4.right= TreeNode(scenario9)

node5.left = TreeNode(scenario10)
node5.right = TreeNode(scenario11)



node6.left = TreeNode(scenario12)
node6.right = TreeNode(scenario13)


node7.left = TreeNode(scenario14)
node7.right = TreeNode(scenario15)


node2.left = (node4)
node2.right = (node5)

node3.left = (node6)
node3.right = (node7)

# Main Tree
root.left= node2 
root.right = node3 