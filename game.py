import pygame
import random
import os
from random import randint, choice
from sys import exit

# 2287039 NEEN RUNGSMAITHONG
"""
    Below is a clickable button class for Pygame.

    Parameters:
    text (str): The text to display on the button.
    text_color (tuple): The color of the text.
    bg_color (tuple): The background color of the button.
    font (str, optional): The font to use. Defaults to "monospace".
    size (int, optional): The font size. Defaults to 15.

    Attributes:
    width (int): The width of the button.
    height (int): The height of the button.
    image (pygame.Surface): The button's image.
    rect (pygame.Rect): The button's rectangle.
    text_rect (pygame.Rect): The text's rectangle.
    clicked (bool): Whether the button is currently clicked.

    Methods:
    is_clicked() -> bool: Returns True if the button is clicked, False otherwise.
"""


class Button(pygame.sprite.Sprite):
    def __init__(
        self, text: str, text_color: tuple, bg_color: tuple, font="monospace", size=15
    ):
        super().__init__()

        button_font = pygame.font.SysFont(font, size)

        self.render_text = button_font.render(text, True, text_color)
        text_width, text_height = self.render_text.get_size()

        # Adjust dimensions based on text size and padding
        self.width = text_width + 20
        self.height = text_height + 20

        # Create the button image (background)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect()  # This defines the button's rectangle

        # center text on the rectangle
        self.text_rect = self.render_text.get_rect(center=self.rect.center)

        # Blit the text onto the button's image
        self.image.blit(self.render_text, self.text_rect)

        # mouse is not clicked
        self.clicked = False

    def is_clicked(
        self,
    ):  # method for an instance of the button class to detect a click
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(
            mouse_pos
        ):  # Check if the mouse cursor is over the button's rectangle (self.rect)

            # check if the left mouse has been clicked that ensure that prolonged clicking will have no effect
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action


# 2253127 JOHN JOE
"""
This is the Game Scenarios Linked List Module
This module implements a linked list data structure to store and manipulate game scenarios.
The ListNode class represents a single node in the linked list, with attributes for the node's value and the next node in the list.
The LinkedList class represents the linked list itself, with methods for appending nodes, converting the linked list data structure to a Python list data type, and a utility functions to get the final scenarios.
The get_game_scenarios function takes a list of game scenarios, shuffles the list randomly, and returns a linked list of the scenarios.

Example:
print(get_game_scenarios(["scenario1", "scenario2", "scenario3", "scenario4"]).to_list())

Note:
This module is designed to handle errors and exceptions, and provides informative error messages to help with debugging.
"""


class ListNode:
    # Constructor to initialize the node object
    def __init__(self, value, next=None):
        """
        Assign data to a node. In our project it will be the game scenario

        Args:
        -value: The value of the node
        -next: The next node in the linked list

        Returns:
        None
        """
        try:
            self.value = value
            # Initialize next as null
            self.next = next
        except Exception as e:
            print(
                "An error occured while creating a node, please check the input values!",
                e,
            )


class LinkedList:
    def __init__(self):
        """
        Initialize the head of the linked list
        """
        try:
            self.head = None
        except Exception as e:
            print("An error occured. No parameter needed!", e)

    def append(self, value):
        """
        Create a new node and append it at the end of the linked list

        Args:
        -value: The value of the node to be appended, here it will be the game scenario

        Returns:
        None
        """
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
            print(
                "An error occured while appending a node, please check the input values!",
                e,
            )

    def to_list(self):
        """
        Convert the linked list to a list

        Args:
        None

        Returns:
        -elements: A list of the elements in the linked list
        """
        try:
            elements = []
            current = self.head
            while current:
                elements.append(current.value)
                current = current.next
            return elements
        except Exception as e:
            print(
                "An error occured while converting the linked list to a list, please check the input values!",
                e,
            )


"""
The following class represents a scenario in the game. Scenario is basically an occurence in the "day" of this game.

Each scenario has a unique number, an associated image for context, and a set of choices with possible outcomes.
The luck difference attribute represents a random value that can affect the outcome of the scenario.

The `set_cases()` method allows setting the caption, choices, and outcomes for the scenario.
The `__str__()`  method returns a string representation of the scenario, including its number.

Example:
    scenario1 = Scenario(1, "path/to/image.jpg")
    scenario1.set_cases(
        "You are at a fork in the road.",
        "Go left",
        "You find a treasure!",
        "You get lost.",
        "Go right",
        "You find a friend!",
        "You get hurt.",
    )
    print(scenario1)  # Output: scenario1
"""


# 5553946 IBRAHIM ALMUTAIRI
class Scenario:
    def __init__(self, scene_num, picture_path: str):
        self.picture_path = picture_path
        self.cases = {}
        self.scene_num = scene_num
        self.luck_diff = randint(1, 20)

    def set_cases(
        self,
        caption: str,
        choice1: str,
        pos_outcome1: str,
        neg_outcome1: str,
        choice2: str,
        pos_outcome2: str,
        neg_outcome2: str,
    ) -> None:
        """Must be two cases"""

        self.caption = caption

        # Case 1
        self.cases["choice1"] = ["pos_outcome1", "pos_outcome2"]

        self.cases["choice1"] = choice1
        self.cases["pos_outcome1"] = pos_outcome1
        self.cases["neg_outcome1"] = neg_outcome1

        # Case 2
        self.cases["choice2"] = choice2
        self.cases["pos_outcome2"] = pos_outcome2
        self.cases["neg_outcome2"] = neg_outcome2

        return None

    def __str__(self):
        output_string = f"scenario{self.scene_num}"

        return output_string


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 12
screen_width = 600
screen_height = 400

"""
The tree and encapsulates every scenario that exists in the game.
The get_path() method will randomise scenarios to be put in the list to be used in the game
"""


# 5553946 IBRAHIM ALMUTAIRI
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ROOT (FIRST LAYER)
scenario1 = Scenario(1, "Graphics/back_door_safe.png")
scenario1.set_cases(
    """The Day Begins.
    Let's get you to work! 
    Which door are you leaving your house through?""",
    # First
    "Front Door",
    f"Yay! That stray cat that always "
    f"\ngouges your eyes out is nowhere in sight!\n\nLuck +{scenario1.luck_diff}",
    f"OW! That cat is here today, you just got scratched ;(\n\nLuck -{scenario1.luck_diff}",
    # Second
    "The Back Door",
    f"Phew, narrowly escaped that nosy neighbour!\n\nLuck +{scenario1.luck_diff}",
    f"Oh no, you tripped over that"
    f"\nbucket of water you left out last night!\n\nLuck -{scenario1.luck_diff}",
)


# SECOND LAYER
scenario2 = Scenario(2, "Graphics/puddle_fail.png")
scenario2.set_cases(
    "While on your way to the train station,"
    "\nyou see a big puddle on the road, what do you do?",
    "Jump over it",
    f"Way to go!"
    f"\nThose long jumps during physical\neducation coming in clutch!\n\nLuck +{scenario2.luck_diff}",
    f"Leg days? 404 not found.\nwhat made you think you could do it?\n\nLuck -{scenario2.luck_diff}",
    "Walk gently",
    f"Phew! You made it, slowly but surely.\n\nLuck +{scenario2.luck_diff}",
    f"Nuh uh those converse wont hold,\nyour feet are taking a bath.\n\nLuck -{scenario2.luck_diff}",
)

scenario3 = Scenario(2, "Graphics/phone_notif.png")
scenario3.set_cases(
    "Ding! Would you like to buy the lottery?",
    "Yes!",
    f"Oh my! You won some money!\n\nLuck +{scenario3.luck_diff}",
    f"Uh oh, that was a scam website :o\n\nLuck -{scenario3.luck_diff}",
    "Nah",
    f"Good job for not getting scammed, you won a prize!\n\nLuck +{scenario3.luck_diff}",
    f"You missed the giveaway they were doing"
    f"\nfor everyone who bought the lottery :(\n\nLuck -{scenario3.luck_diff}",
)

# THIRD LAYER
scenario4 = Scenario(3, "Graphics/wait_for_train.png")
scenario4.set_cases(
    "At the train station," "\nyou just bought coffee, oh no! that train is here!",
    "Wait for next train",
    f"The next train came early!"
    f"\nYou enjoyed your coffee and got to work on time.\n\nLuck +{scenario4.luck_diff}",
    f"the train was terminated :|\n\nLuck -{scenario4.luck_diff}",
    "RUN FOR IT!!",
    f"You caught the train! Off to work we go!\n\nLuck +{scenario4.luck_diff}",
    f"You caught the train, but at what cost..."
    f"\nYou are now drenched in coffee.\n\nLuck -{scenario4.luck_diff}",
)

scenario5 = Scenario(3, "Graphics/unexpected_project.png")
scenario5.set_cases(
    "Your boss just offered you a challenging project"
    "\nthat could make or break you! What will you do?",
    # First
    "Accept the project",
    f"The project made you all right! Way to go!\n\nLuck +{scenario5.luck_diff}",
    f"The project broke you :/\n\nLuck -{scenario5.luck_diff}",
    # Second
    "Decline the project",
    f"Phew! Dodged a bullet, that was never gonna work!\n\nLuck +{scenario5.luck_diff}",
    f"Opportunity of a lifetime, down the drain!"
    f"\n Your boss gave it to your work nemesis instead!\n\nLuck -{scenario5.luck_diff}",
)

scenario6 = Scenario(3, "Graphics/unexpected_client.png")
scenario6.set_cases(
    "A client decides to visit the office unexpectedly.\nWhat will you do?",
    # First
    "Greet the client",
    f"Oh my! turns out he's a big shot,"
    f"\nand you've got his name under yours!\n\nLuck +{scenario6.luck_diff}",
    f"'Uh- is this not the toilet? Sorry.'"
    f"\n-The man who is decidedly not a client.\n\nLuck -{scenario6.luck_diff}",
    # Second
    "Let him reschedule",
    f"Turns out he's a scammer! "
    f"\nGood thing you didn't meet with him.\n\nLuck +{scenario6.luck_diff}",
    f"The man was a big shot and you missed it :o\n\nLuck -{scenario6.luck_diff}",
)

scenario7 = Scenario(3, "Graphics/fire_drill.png")
scenario7.set_cases(
    "Your office conducts an unexpected fire safety drill."
    "\nDo you take it seriously?",
    # First
    "Take it seriously",
    f"Whoa, thought that was real.\n\nLuck +{scenario7.luck_diff}",
    f"You missed out on the chance to talk to your crush!\n\nLuck -{scenario7.luck_diff}",
    # Second
    "Chit-chat",
    f"Told the best joke ever. Everyone loves me.\n\nLuck +{scenario7.luck_diff}",
    f"Shoot, your boss is super uptight\nand is shooting you dirty looks\n\nLuck -{scenario7.luck_diff}",
)

scenario8 = Scenario(4, "Graphics/networking_event.png")
scenario8.set_cases(
     "You receive a last-minute invitation to a networking event."
     "\nDo you attend or stay home?",
     "Attend the event",
     f"Ha! Got a huge client right then and there!\n\nLuck +{scenario8.luck_diff}",
     f"Why host an event like this"
     f"\nwhen watching paint dry have the same effect?\n\nLuck -{scenario8.luck_diff}",
     "Stay home",
     f"Apparently it was a prank by your mate,"
     f"\nnever gonna get me in this life, pal!\n\nLuck +{scenario8.luck_diff}",
     f"Your work nemesis got\na new client from the event! \n\nLuck -{scenario8.luck_diff}"
)

# 2287039 NEEN + 2253127 JOE fitted the tree logic to match the scenarios and gameplay
# FORTH LAYER

scenario9 = Scenario(4, "Graphics/meeting.png")
scenario9.set_cases(
    "You receive a last-minute request \nto join an additional meeting,"
    "\nDo you attend the meeting or decline?",
    "Attend",
    f"Finally got your chance to really\ndazzle in the meeting room today!\n\nLuck +{scenario9.luck_diff}",
    f"The meeting is unproductive,"
    f"\nand you fall behind on your work :(\n\nLuck -{scenario9.luck_diff}",
    "Decline",
    f"Boss said ouch but he fills you in anyway."
    f"\nPays to be a favorite I guess!\n\nLuck +{scenario9.luck_diff}",
    f"Could've been your chance to shine :("
    f"\nChance was given to your work nemesis instead.\n\nLuck -{scenario9.luck_diff}",
)

scenario10 = Scenario(4, "Graphics/exercise.png")
scenario10.set_cases(
     "Feeling energetic, you consider going for \nan evening jog. Do you hit the park or the gym treadmill?",
     "Jog in the park",
     f"Met your crush at the park,\nmight start running every day tbh.\n\nLuck +{scenario10.luck_diff}",
     f"It starts raining so heavily all of a sudden.\nWelp.\n\nLuck -{scenario10.luck_diff}",
     "Gym treadmill",
     f"You're a runner, you're a track star. \n\nLuck +{scenario10.luck_diff}",
     f"The gym SMELLED SO BAD. YUCK. \n\nLuck -{scenario10.luck_diff}",
 )

scenario11 = Scenario(4, "Graphics/grocery.png")
scenario11.set_cases(
     "You realize you need groceries. Do you stop\nby the store or order delivery?",
     "Grocery Store",
     f"What a steal! Everything you need is on sale!\n\nLuck +{scenario11.luck_diff}",
     f"The store is super crowded,\ncould've been home by now :/\n\nLuck -{scenario11.luck_diff}",
     "Delivery.",
     f"It came with an extra saving deal!!\n\nLuck +{scenario11.luck_diff}",
     f"The delivery is late and missing items."
     f"\nGuess you'll have to live without eggs for the week.\n\nLuck -{scenario11.luck_diff}",
 )

scenario12 = Scenario(4, "Graphics/dinner.png")
scenario12.set_cases(
    "It's time for dinner, but you're not in\nthe mood to cook. Do you order in or go out to eat?",
    "Order in",
    f"Mhmm Best Korean place in town!!\n\nLuck +{scenario12.luck_diff}",
    f"They got your order wrong...\n\nLuck -{scenario12.luck_diff}",
    "Eat out",
    f"Nothing beats a good meal with good vibes!\n\nLuck +{scenario12.luck_diff}",
    f"The restaurant is full.\nWaiter said next queue is in 3hrs.\n\nLuck -{scenario12.luck_diff}",
)

scenario13 = Scenario(4, "Graphics/relax.png")
scenario13.set_cases(
     "You feel the need to unwind.\nDo you read a book or watch a movie?",
     "Read a book",
     f"Instant favorite book. SO GOOD!\n\nLuck +{scenario13.luck_diff}",
     f"Words.. so many words.. \n\nLuck -{scenario13.luck_diff}",
     "Watch a movie",
     f"Your favorite actor was a surprise cameo!!\n\nLuck +{scenario13.luck_diff}",
     f"Your mum called but you didn't\nhear your phone ring. She's mad now.\n\nLuck -{scenario13.luck_diff}",
 )

scenario14 = Scenario(4, "Graphics/online_class.png")
scenario14.set_cases(
     "You remember you’ve signed up for an online course. "
     "\nDo you want to catch up on the lessons?",
     "Catch up",
     f"Got a special achievement, go you!\n\nLuck +{scenario14.luck_diff}",
     f"You were so caught up in the course,\nyou forgot to complete your work!\n\nLuck -{scenario14.luck_diff}",
     "Relax",
     f"You take the evening off,\nand now you're more productive than ever!\n\nLuck +{scenario14.luck_diff}",
     f"You just lost your 10-day streak!!!\n\nLuck -{scenario14.luck_diff}",
 )

scenario15 = Scenario(4, "Graphics/local_class.png")
scenario15.set_cases(
     "You have the option to attend a \nlocal evening class. Which will you choose?",
     "Yoga",
     f"Met your crush at the class."
     f"\nbest. yoga. class. ever.\n\nLuck +{scenario15.luck_diff}",
     f"It gives you SUCH cramps the next day.\n\nLuck -{scenario15.luck_diff}",
     "Cooking",
     f"You learn a new recipe \nthat becomes a new favorite at home!!\n\nLuck +{scenario15.luck_diff}",
     f"You dropped the whole bottle of salt,\nwho knew mushroom soup was so tricky?\n\nLuck -{scenario15.luck_diff}",
 )


# Scenarios Tree
Node1 = TreeNode(scenario1)
# Second Level
Node2 = TreeNode(scenario2)
Node3 = TreeNode(scenario3)

# Third Level
Node4 = TreeNode(scenario4)
Node5 = TreeNode(scenario5)

Node6 = TreeNode(scenario6)
Node7 = TreeNode(scenario7)

# Fourth Level
Node8 = TreeNode(scenario8)
Node9 = TreeNode(scenario9)

Node10 = TreeNode(scenario10)
Node11 = TreeNode(scenario11)

Node12 = TreeNode(scenario12)
Node13 = TreeNode(scenario13)

Node14 = TreeNode(scenario14)
Node15 = TreeNode(scenario15)


# 5532173 REAGAN PIUS : Refactored Tree to build with Lambda

# building the tree
root = Node1

# 2ND LEVEL
root.left, root.right = Node2, Node3

# 3RD & 4TH LEVELS
nodes = [Node2, Node3, Node4, Node5, Node6, Node7]
children = [
    Node4,
    Node5,
    Node6,
    Node7,
    Node8,
    Node9,
    Node10,
    Node11,
    Node12,
    Node13,
    Node14,
    Node15,
]

"""This list function converts the iterator produced by map into a list to force map to apply the lambda function to all the elements."""
list(
    map(
        lambda x, y: setattr(x, "left", y[0]) or setattr(x, "right", y[1]),
        nodes,
        zip(*[children[i::2] for i in range(2)]),
    )
)
"""This is a list comprehension that creates two lists from the children list.
        The first list contains every other element from the children list, starting from the first element (children[0::2]), 
        and the second list contains every other element, starting from the second element (children[1::2]"""


def get_path(root):
    if root is None:
        return []
    path = [root.data]
    if root.left is None and root.right is None:
        return path
    else:
        if choice([True, False]):
            return path + get_path(root.left)
        else:
            return path + get_path(root.right)


def get_game_scenarios(instances_list):
    """
    Create a linked list of the game scenarios

    Args:
    -instances: A list of the game scenarios

    Returns:
    -linked_list: A linked list of the game scenarios
    """
    try:
        linked_list = LinkedList()
        for instance in instances_list:
            linked_list.append(instance)
        return linked_list
    except Exception as e:
        print("List needed to be passed, please check input.", e)


# 2253127 JOE, 2287039 NEEN,5532173 REAGAN, 5553946 IBRAHIM
class Game:
    """
    This is the main game logic with event handlers and methods to display the screen on which the events are occuring.
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LUCKOMETER")
        self.state = "menu"
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", FONT_SIZE)
        self.luck_score = randint(5, 20)
        self.scenarios_Linked_list = None
        self.current_state = None
        self.buttons = {}
        self.initialise_buttons()
        self.current_screen = ""
        self.logfile = open("luckometer.log", "w")  # Event Logging File
        self.main_music = pygame.mixer.Sound(os.path.join("audio/intro.wav"))
        self.end_music = pygame.mixer.Sound(os.path.join("audio/not-really-lost.wav"))

    # 5532173 REAGAN PIUS Displaying Section
    def display_text(
        self,
        text: str,
        text_color: tuple,
        bg_color=None,
        x="centre",
        y="centre",
        font="comic sans",
        size=FONT_SIZE,
    ) -> None:
        font = pygame.font.SysFont(font, size)
        lines = text.split("\n")
        line_surfaces = [
            font.render(line, True, text_color, bg_color) for line in lines
        ]
        # Calculating the x and y coordinates to center the instruction on the screen
        if x == "centre":
            x = (
                screen_width
                - max(line_surface.get_width() for line_surface in line_surfaces)
            ) / 2
        if y == "centre":
            y = (
                screen_height
                - sum(line_surface.get_height() for line_surface in line_surfaces)
            ) / 2

        # Finally blitting each line to the screen
        for i, line_surface in enumerate(line_surfaces):
            self.screen.blit(line_surface, (x, y + i * (line_surface.get_height())))

        return None

    # 5553946 IBRAHIM ALMUTAIRI
    def display_scenario(self, scenario: Scenario) -> None:
        self.create_button(f"s{scenario.scene_num}_choice1", scenario.cases["choice1"])
        self.create_button(f"s{scenario.scene_num}_choice2", scenario.cases["choice2"])
        self.screen.fill("white")
        self.display_text(f"Luck Score: {self.luck_score}", BLACK, x=10, y=10, size=12)
        self.display_text(scenario.caption, BLACK, x=45, y=40, size=20)
        self.display_image(scenario.picture_path, 25, 137)
        self.draw_button(
            f"s{scenario.scene_num}_choice1",
            320,
            186,
        )
        self.draw_button(f"s{scenario.scene_num}_choice2", 320, 246)
        self.draw_button("home", 530, 10)

        self.log_event(f"{scenario} displayed")
        self.current_screen = f"{scenario}"
        return None

    # 5553946 IBRAHIM
    def display_image(self, image_path: str, x: int, y: int) -> None:
        img = pygame.image.load(image_path).convert()
        self.screen.blit(img, (x, y))
        return None

    # 2287039 NEEN RUNGSMAITHONG
    def log_event(self, event) -> None:
        """Logs events and the timestamp when they occur."""
        timestamp = (
            pygame.time.get_ticks()
        )  # Gets the number of milliseconds since pygame.init() was called
        log_message = f"{timestamp / 1000}s: {event}\n"
        self.logfile.write(log_message)
        print(log_message)
        return None

    def initialise_scenarios(self) -> None:
        scenario_list = get_path(Node1)
        self.scenarios_Linked_list = get_game_scenarios(scenario_list)
        if self.scenarios_Linked_list and self.scenarios_Linked_list.head:
            self.current_state = self.scenarios_Linked_list.head
        return None

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.log_event("QUIT CLICKED")
                pygame.quit()
                self.logfile.close()
                exit()

            if self.current_screen in ("start", "end"):
                if self.buttons["quit"].is_clicked():
                    self.log_event("QUIT BUTTON CLICKED")
                    pygame.quit()
                    self.logfile.close()
                    exit()

            if self.current_screen == "start":
                if self.buttons["start"].is_clicked():
                    if not self.current_state:  # only execute 'start' if scenarios have yet to be initialised
                        self.log_event("START BUTTON CLICKED")
                        self.display_instructions_screen()
                    else:
                        self.display_text(
                            "You have already started the game.\npress SPACE and click resume.",
                            BLACK,
                            WHITE,
                            size=17)
                        self.log_event("Error message shown")

                if self.buttons["resume"].is_clicked():
                    self.log_event("RESUME BUTTON CLICKED")
                    try:
                        self.display_scenario(self.current_state.value)

                    except AttributeError:  # handle error when self.current_state is None
                        self.display_text(
                            "You have not started the game.\npress SPACE and click start.",
                            BLACK,
                            WHITE,
                            size=17)
                        self.log_event("Error message shown")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.log_event("SPACEBAR PRESSED")
                    self.display_start_screen()

            if self.current_screen == "instruction":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.log_event("SPACEBAR PRESSED")

                    # 5532173 REAGAN PIUS Add Music Accompaniment and Handle Errors w/lambda
                    pygame.mixer.Sound.set_volume(self.main_music, 0.3)
                    play_music = lambda music: (
                        (lambda: music.play(loops=6))()
                        if music
                        else (lambda: self.log_event("Error playing music"))()
                    )
                    play_music(self.main_music)
                    self.log_event("Intro Music Playing")
                    self.initialise_scenarios()
                    self.display_scenario(self.current_state.value)

            if "scenario" in self.current_screen:
                if self.buttons["home"].is_clicked():
                    self.log_event("HOME BUTTON CLICKED")
                    self.display_start_screen()

            if self.current_screen == "scenario1":
                if self.buttons["s1_choice1"].is_clicked():
                    self.log_event("s1_choice1 CLICKED")
                    self.display_outcome(1)
                if self.buttons["s1_choice2"].is_clicked():
                    self.log_event("s1_choice2 CLICKED")
                    self.display_outcome(2)
                if self.buttons["continue"].is_clicked():
                    self.log_event("CONTINUE CLICKED")
                    self.current_state = self.current_state.next
                    self.display_scenario(self.current_state.value)

            if self.current_screen == "scenario2":
                if self.buttons["s2_choice1"].is_clicked():
                    self.log_event("s2_choice1 CLICKED")
                    self.display_outcome(1)
                if self.buttons["s2_choice2"].is_clicked():
                    self.log_event("s2_choice2 CLICKED")
                    self.display_outcome(2)
                if self.buttons["continue"].is_clicked():
                    self.log_event("CONTINUE CLICKED")
                    self.current_state = self.current_state.next
                    self.display_scenario(self.current_state.value)

            if self.current_screen == "scenario3":
                if self.buttons["s3_choice1"].is_clicked():
                    self.log_event("s3_choice1 CLICKED")
                    self.display_outcome(1)
                if self.buttons["s3_choice2"].is_clicked():
                    self.log_event("s3_choice2 CLICKED")
                    self.display_outcome(2)
                if self.buttons["continue"].is_clicked():
                    self.log_event("CONTINUE CLICKED")
                    self.current_state = self.current_state.next
                    self.display_scenario(self.current_state.value)

            if self.current_screen == "scenario4":
                if self.buttons["s4_choice1"].is_clicked():
                    self.log_event("s4_choice1 CLICKED")
                    self.display_outcome(1)
                if self.buttons["s4_choice2"].is_clicked():
                    self.log_event("s4_choice2 CLICKED")
                    self.display_outcome(2)
                if self.buttons["continue"].is_clicked():
                    self.log_event("CONTINUE CLICKED")

                    # 5532173 REAGAN PIUS Second Music Accompaniment and Handle Errors w/lambda
                    self.main_music.stop()
                    self.log_event("Intro Music Stopping")
                    end_music = lambda music: (
                        (lambda: music.play())()
                        if music
                        else (lambda: self.log_event("Error playing music"))()
                    )
                    end_music(self.main_music)
                    pygame.mixer.Sound.set_volume(self.end_music, 0.3)
                    self.end_music.play()
                    self.log_event("End Music Playing")
                    self.display_end_screen()

            if self.current_screen == "end":
                if self.buttons["play_again"].is_clicked():
                    self.log_event("PLAY AGAIN BUTTON CLICKED")
                    self.end_music.stop()
                    self.log_event("End Music Stopping")
                    self.luck_score = randint(5, 20)  # recalibrate initial luck score
                    self.current_state = None  # reset scenarios
                    self.display_start_screen()
        return None

    # NEEN 2287039
    def create_button(
        self,
        name: str,
        text: str,
        text_color=(167, 66, 132),
        bg_color=(221, 229, 13),
        font="monospace",
        size=20,
    ) -> None:
        """
        :param name: name of button
        :param text: text to be put as button
        :param text_color: default color set to (167,66,132)->(dark purple)
        :param bg_color: default bg color set to (221,229,13)->(neon yellow)
        :param font: default font set to monospace
        :param size: default font size set to 20

        :return: None
        """
        button = Button(text, text_color, bg_color, font, size)
        self.buttons[name] = button  # each button added to dictionary to be used in handle_events()

        return None

    def draw_button(self, name: str, x="centre", y="centre") -> None:
        """
        :param name: name of button to be drawn on screen
        :param x: default set to align centre
        :param y: default set to align centre

        :return: None
        """
        # setting x and y coordinates
        if x == "centre":
            x = (screen_width - self.buttons[name].width) / 2
        if y == "centre":
            y = (screen_height - self.buttons[name].height) / 2

        self.buttons[name].rect.topleft = (x, y)
        self.screen.blit(self.buttons[name].image, (self.buttons[name].rect.x, self.buttons[name].rect.y))

        return None

    def initialise_buttons(self):
        self.create_button("start", "START")
        self.create_button("resume", "RESUME")
        self.create_button("quit", "QUIT")
        self.create_button("play_again", "PLAY AGAIN")
        self.create_button("home", "HOME", size=15)
        self.create_button("continue", "CONTINUE")

    # 2287039 NEEN
    def display_start_screen(self):
        self.display_image("Graphics/title_screen.png", 0, 0)
        self.draw_button("start", y=176)
        self.draw_button("resume", y=225)
        self.draw_button("quit", y=274)

        self.log_event("START SCREEN DISPLAYED")
        self.current_screen = "start"

    # 5532173 REAGAN PIUS
    def display_instructions_screen(self):
        self.display_image("Graphics/instructions.png", 0, 0)

        # Defining the instructions text
        instruction = """
        The game begins at home, you start off with a randomised 
        luck score(between 5 to 20). Each decision you make 
        will have an impact that can be anything from 1 to 20!
        Remember, this is a game of luck, so no matter how sound
        your choice may seem, there is always a twist. 
        Your aim is to have over 50 luck at the end of the game. 
        Good Luck!
        """

        self.display_text(instruction, WHITE, x=20, size=17)
        self.log_event("INSTRUCTIONS SCREEN DISPLAYED")
        self.current_screen = "instruction"

    # 2287039 NEEN
    def display_outcome(self, choice_num):

        # nested function in order to retrieve the key(eg. 'pos_outcome1') given the outcome(eg. 'Won the lottery')
        def get_key(search_value):
            for key, value in self.current_state.value.cases.items():
                if value == search_value:
                    return key
            return None

        outcomes = [
            self.current_state.value.cases[f"pos_outcome{choice_num}"],
            self.current_state.value.cases[f"neg_outcome{choice_num}"],
        ]
        outcome = choice(outcomes)

        if "pos" in get_key(outcome):
            self.luck_score += self.current_state.value.luck_diff
            self.log_event("positive outcome displayed")
        if "neg" in get_key(outcome):
            self.luck_score -= self.current_state.value.luck_diff
            self.log_event("negative outcome displayed")

        self.screen.fill(WHITE)
        self.display_text(f"Luck Score: {self.luck_score}", BLACK, x=10, y=10, size=12)
        self.display_text(outcome, BLACK, size=20)
        self.draw_button("continue", 448, 340)

    # 5532173 REAGAN PIUS
    def display_end_screen(self):
        self.display_image("Graphics/end_screen.png", 0, 0)

        if self.luck_score > 50:
            self.display_text(
                f"Your Final Luck Score is {self.luck_score}.\nIt's your lucky day!",
                BLACK,
                WHITE,
                y=100,
                size=20,
            )

        if 20 <= self.luck_score <= 50:
            self.display_text(
                f"Your Final Luck Score is {self.luck_score}."
                f"\nIt's just like any other day.",
                BLACK,
                WHITE,
                y=100,
                size=20,
            )

        if self.luck_score < 20:
            self.display_text(
                f"Your Final Luck Score is {self.luck_score}."
                f"\nUh oh, a black cat may be around the corner!",
                BLACK,
                WHITE,
                y=100,
                size=20,
            )

        self.draw_button("play_again", y=176)
        self.draw_button("quit", y=225)

        self.log_event("END SCREEN DISPLAYED")
        self.current_screen = "end"

    def run(self):
        self.screen.fill((0, 0, 0))
        self.current_screen = "start"
        self.display_start_screen()

        while True:

            self.handle_events()
            pygame.display.flip()
            self.clock.tick(60)


# checks that the program runs only as an executable and not as an import
if __name__ == "__main__":
    game = Game()
    game.run()
