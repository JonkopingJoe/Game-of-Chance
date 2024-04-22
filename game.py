import pygame
import os
from random import randint, choice, shuffle
from scenario import Scenario
from button import Button
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 12
screen_width = 600
screen_height = 400


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
    "Yay! That stray cat that always gouges your eyes out is nowhere in sight!",
    "OW! That cat is here today, you just got scratched ;(",
    # Second
    "The Back Door",
    f"Phew, narrowly escaped that nosy neighbour!",
    f"Oh no, you tripped over that bucket of water you left out last night!"
    )


# SECOND LAYER
scenario2 = Scenario(2, "Graphics/puddle_fail.png")
scenario2.set_cases(
    "While on your way to the train station,"
    "y\nou see a big puddle on the road, what do you do?",
    "Jump over it",
    f"Way to go!\nThose long jumps during physical education coming in clutch!",
    f"Leg days? 404 not found.\nwhat made you think you could do it?",
    "Walk gently",
    f"Phew! You made it, slowly but surely.",
    f"Nuh uh those converse wont hold,\nyour feet are taking a bath."
    )

scenario3 = Scenario(2, "Graphics/phone_notif.png")
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
scenario4 = Scenario(3, "Graphics/wait_for_train.png")
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

scenario5 = Scenario(3, "Graphics/unexpected_project.png")
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

scenario6 = Scenario(3, "Graphics/unexpected_client.png")
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

scenario7 = Scenario(3, 'Graphics/fire_drill.png')
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

scenario8 = Scenario(4, "Graphics/networking_event.png")
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
scenario9 = Scenario(4, "Graphics/meeting.png")
scenario9.set_cases(
    "You receive a last-minute request to join an additional meeting,"
    "\nbut you’re already swamped with work. Do you attend the meeting or decline?",
    "Attend",
    "The meeting turns out to be crucial, and your input is highly valued.",
    "The meeting is unproductive, and you fall behind on your work :(",
    "Decline",
    "You made significant progress on your projects by declining. ",
    "You missed out on important information shared in the meeting!!")

# Scenario 3: Evening Jog
scenario10 = Scenario(4, "Graphics/exercise.png")
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
scenario11 = Scenario(4, "Graphics/grocery.png")
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
scenario12 = Scenario(4, "Graphics/dinner.png")
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
scenario13 = Scenario(4, "Graphics/relax.png")
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
scenario14 = Scenario(4, "Graphics/online_class.png")
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
scenario15 = Scenario(4, "Graphics/local_class.png")
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

# building the tree
root = TreeNode(scenario1)
# 2ND LEVEL
root.left = Node2
root.right = Node3
# 3RD LEVEL
Node2.left = Node4
Node2.right = Node5

Node3.left = Node6
Node3.right = Node7
#4TH LEVEL
Node4.left = Node8
Node4.right = Node9

Node5.left = Node10
Node5.right = Node11

Node6.left = Node12
Node6.right = Node13

Node7.left = Node14
Node7.right = Node15


def get_path(root):
    if root is None:
        return []
    path = [root.data]
    if root.left is None and root.right is None:
        return path
    elif root.left is None:
        return path + get_path(root.right)
    elif root.right is None:
        return path + get_path(root.left)
    else:
        if choice([True, False]):
            return path + get_path(root.left)
        else:
            return path + get_path(root.right)


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
            print("An error occured while appending a node, please check the input values!", e)

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
        shuffle(instances_list)
        linked_list = LinkedList()
        for instance in instances_list:
            linked_list.append(instance)
        return linked_list
    except Exception as e:
        print("List needed to be passed, please check input.", e)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LUCKOMETER")
        self.state = "menu"
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", FONT_SIZE)
        self.luck_score = randint(0, 20)
        self.scenarios_Linked_list = None
        self.current_state = None
        self.buttons = {}
        self.initialise_buttons()
        self.current_screen = ""
        self.logfile = open("luckometer.log", "w")  # Event Logging File
        self.main_music = pygame.mixer.Sound(os.path.join("./audio", "intro.wav"))
        self.end_music = pygame.mixer.Sound(
            os.path.join("./audio", "not-really-lost.wav")
        )

    # Displaying Section
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
                screen_width - max(line_surface.get_width() for line_surface in line_surfaces)) / 2
        if y == "centre":
            y = (screen_height - sum(line_surface.get_height() for line_surface in line_surfaces)) / 2

        # Finally blitting each line to the screen
        for i, line_surface in enumerate(line_surfaces):
            self.screen.blit(line_surface, (x, y + i * (line_surface.get_height())))

        return None

    def display_scenario(self, scenario: Scenario) -> None:
        self.create_button(f"s{scenario.scene_num}_choice1", scenario.cases["choice1"])
        self.create_button(f"s{scenario.scene_num}_choice2", scenario.cases["choice2"])
        self.screen.fill("white")
        self.display_text(f"Luck Score: {self.luck_score}", BLACK, x=10, y=10, size=12)
        self.display_text(scenario.caption, BLACK, x=45, y=40, size=20)
        self.display_image(scenario.picture_path, 25, 137)
        self.draw_button(f"s{scenario.scene_num}_choice1", 320, 186,)
        self.draw_button(f"s{scenario.scene_num}_choice2", 320, 246)
        self.draw_button("home", 530, 10)

        self.log_event(f"{scenario} displayed")
        self.current_screen = f"{scenario}"
        return None

    def display_image(self, image_path: str, x: int, y: int) -> None:
        img = pygame.image.load(image_path).convert()
        self.screen.blit(img, (x, y))
        return None

    def log_event(self, event) -> None:
        """Logs events and the timestamp when they occur."""
        timestamp = (
            pygame.time.get_ticks())  # Gets the number of milliseconds since pygame.init() was called
        log_message = f"{timestamp / 1000}s: {event}\n"
        self.logfile.write(log_message)
        print(log_message)
        return None

    def initialise_scenarios(self):
        self.scenarios_Linked_list = get_game_scenarios(get_path(Node1))
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
                    if not self.current_state:
                        self.log_event("START BUTTON CLICKED")
                        self.display_instructions_screen()
                    else:
                        self.display_text(
                            "You have already started the game.\npress SPACE and click resume.",
                            BLACK,
                            WHITE,
                            size=17,
                        )
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.log_event("SPACEBAR PRESSED")
                            self.display_start_screen()

                if self.buttons["resume"].is_clicked():
                    self.log_event("RESUME BUTTON CLICKED")
                    try:
                        self.display_scenario(self.current_state.value)

                    except AttributeError:
                        self.display_text(
                            "You have not started the game.\npress SPACE and click start.",
                            BLACK,
                            WHITE,
                            size=17,
                        )
                        self.log_event("Error message shown")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.log_event("SPACEBAR PRESSED")
                    self.display_start_screen()

            if self.current_screen == "instruction":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.log_event("SPACEBAR PRESSED")
                    self.initialise_scenarios()

                    # Add Music Accompaniment
                    pygame.mixer.Sound.set_volume(self.main_music, 0.3)
                    self.main_music.play(loops=6)
                    self.log_event("Intro Music Playing")
                    if self.scenarios_Linked_list and self.scenarios_Linked_list.head:
                        self.current_state = self.scenarios_Linked_list.head
                        self.display_scenario(self.current_state.value)

            if (
                "scenario" in self.current_screen
                or self.current_screen == "instruction"
            ):
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

                    # Second Music Accompaniment
                    self.main_music.stop()
                    self.log_event("Intro Music Stopping")
                    pygame.mixer.Sound.set_volume(self.end_music, 0.3)
                    self.end_music.play()
                    self.log_event("End Music Playing")
                    self.display_end_screen()

            if self.current_screen == "end":
                if self.buttons["play_again"].is_clicked():
                    self.log_event("PLAY AGAIN BUTTON CLICKED")
                    self.end_music.stop()
                    self.log_event("End Music Stopping")
                    self.luck_score = randint(-20, 20)
                    self.current_state = None
                    self.display_start_screen()
        return None

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
        :param text_color: default color set to (167,66,132) (dark purple)
        :param bg_color: default bg color set to (221,229,13) (neon yellow)
        :param font: default font set to monospace
        :param size: default font size set to 20

        :return: None
        """
        button = Button(text, text_color, bg_color, font, size)
        self.buttons[name] = button  # button added to dictionary to be used in handle_events(self)

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
        self.screen.blit(
            self.buttons[name].image,
            (self.buttons[name].rect.x, self.buttons[name].rect.y))

        return None

    def initialise_buttons(self):
        self.create_button("start", "START")
        self.create_button("resume", "RESUME")
        self.create_button("quit", "QUIT")
        self.create_button("play_again", "PLAY AGAIN")
        self.create_button("home", "HOME", size=15)
        self.create_button("continue", "CONTINUE")

    def display_start_screen(self):
        self.display_image("Graphics/title_screen.png", 0, 0)
        self.draw_button("start", y=176)
        self.draw_button("resume", y=225)
        self.draw_button("quit", y=274)

        self.log_event("START SCREEN DISPLAYED")
        self.current_screen = "start"

    def display_instructions_screen(self):
        self.display_image("Graphics/instructions.png", 0, 0)

        # Defining the instructions text
        instruction = """
        The game starts at home, and the day begins. 
        You start off with a randomised luck score, 
        and each decision you make will have an effect.
        Remember, this is a game of luck, so no matter how sound
        your choice may seem, there is always a twist. 
        Your aim is to have over 50 luck at the end of the game. 
        Good Luck!
        """

        self.display_text(instruction, WHITE, size=17)
        self.log_event("INSTRUCTIONS SCREEN DISPLAYED")
        self.current_screen = "instruction"

    def display_outcome(self, choice_num):
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

        if 20 < self.luck_score < 50:
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


game = Game()
game.run()
