import pygame
import os
from random import randint, choice
from scenario import Scenario
from button import Button
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 12
screen_width = 600
screen_height = 400


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
                "An error occurred while creating a node, please check the input values!",
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
            print("An error occurred. No parameter needed!", e)

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
                "An error occurred while appending a node, please check the input values!",
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
                "An error occurred while converting the linked list to a list, please check the input values!",
                e,
            )

    def traverse(self):
        """
        Traverse the linked list to test the code

        Args:
        None

        Returns:
        None
        """
        try:
            current = self.head
            while current:
                print(current.value)
                current = current.next
        except Exception as e:
            print(
                "An error occurred while traversing the linked list, please check the input values!",
                e,
            )


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
        self.initialize_game_scenarios_list()
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

        if x == "centre":
            # Calculating the x and y coordinates to center the instruction on the screen with padding
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

    def display_scenario(self, scenario: Scenario) -> None:
        self.create_button(f"s{scenario.scene_num}_choice1", scenario.cases["choice1"])
        self.create_button(f"s{scenario.scene_num}_choice2", scenario.cases["choice2"])
        self.screen.fill("white")
        self.display_text(f"Luck Score: {self.luck_score}", BLACK, x=10, y=10, size=12)
        self.display_text(scenario.caption, BLACK, x=45, y=40, size=20)
        self.display_image(scenario.picture_path, 25, 137)
        self.draw_button(f"s{scenario.scene_num}_choice1", 186, 320)
        self.draw_button(f"s{scenario.scene_num}_choice2", 246, 320)
        self.draw_button("home", 10, 530)

        self.log_event(f"{scenario} displayed")
        self.current_screen = f"{scenario}"

    def display_image(self, image_path: str, x: int, y: int) -> None:
        img = pygame.image.load(image_path).convert()
        self.screen.blit(img, (x, y))
        return None

    def initialize_game_scenarios_list(self) -> LinkedList:
        """
        This method initializes the game scenarios linked list and returns it.
        Each scenario will be a node in a linked list.
        You can traverse the list by calling node.next.
        """

        # scenario one
        scenario1 = Scenario(1, "Graphics/scenario1_leave_house.png")
        scenario1.set_cases(
            """The Day Begins.
            Let’s get you to work! 
            Which door are you leaving your house through?""",
            # First
            "The Front Door",
            f"Yay! That stray cat that always gouges"
            f"\nyour eyes out is nowhere in sight!\n\nLuck +{scenario1.luck_diff}",
            f"OW! That cat is here today, you just got scratched ;(\n\nLuck -{scenario1.luck_diff}",
            # Second
            "The Back Door",
            f"Phew, narrowly escaped that nosy neighbour!\n\nLuck +{scenario1.luck_diff}",
            f"Oh no, you tripped over that bucket of\nwater you left out last night!\n\nLuck -{scenario1.luck_diff}",
        )

        # scenario two
        scenario2 = Scenario(2, "Graphics/puddle_fail.png")
        scenario2.set_cases(
            """While on your way to the train station,
            you see a big puddle on the road, what do you do?""",
            "Jump over it",
            f"Way to go!\nThose long jumps during physical education coming in clutch!\n\nLuck +{scenario2.luck_diff}",
            f"Leg days? 404 not found.\nwhat made you think you could do it?\n\nluck -{scenario2.luck_diff}",
            "Walk gently",
            f"Phew! You made it, slowly but surely.\n\nLuck +{scenario2.luck_diff}",
            f"Nuh uh those converse wont hold,\nyour feet are taking a bath.\n\nLuck -{scenario2.luck_diff}",
        )

        # scenario three
        scenario3 = Scenario(3, "Graphics/phone_notif.png")
        scenario3.set_cases(
            "Ding! Would you like to buy the lottery?",
            "Yes!",
            f"Oh my! You won some money!\n\nLuck +{scenario3.luck_diff}",
            f"Uh oh, that was a scam website :o\n\nLuck -{scenario3.luck_diff}",
            "Nah",
            f"Good job for not getting scammed, you won a prize!\n\nLuck +{scenario3.luck_diff}",
            f"You missed they giveaway they were doing"
            f"\nfor everyone who bought lottery :(\n\nLuck -{scenario3.luck_diff}")

        # scenario four
        scenario4 = Scenario(4, "Graphics/wait_for_train.png")
        scenario4.set_cases(
            """At the train station,
            you just bought coffee, oh no! that train is here!""",
            "Wait for next train",
            f"The next train came early!"
            f"\nYou enjoyed your coffee and got to work on time.\n\nLuck +{scenario4.luck_diff}",
            f"the train was terminated :|\n\nLuck -{scenario4.luck_diff}",
            "RUN!!",
            f"You caught the train! Off to work we go!\n\nLuck +{scenario4.luck_diff}",
            f"You caught the train, but at what cost..."
            f"\nYou are now drenched in coffee.\n\nLuck -{scenario4.luck_diff}",
        )

        self.scenarios_Linked_list = get_game_scenarios(
            [scenario1, scenario2, scenario3, scenario4])

        return self.scenarios_Linked_list

    def log_event(self, event):
        """Logs events and the timestamp when they occur."""
        timestamp = (
            pygame.time.get_ticks()
        )  # Gets the number of milliseconds since pygame.init() was called
        log_message = f"{timestamp / 1000}s: {event}\n"
        self.logfile.write(log_message)
        print(log_message)

    def handle_events(self):
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

    def create_button(
        self,
        name: str,
        text: str,
        text_color=(167, 66, 132),
        bg_color=(221, 229, 13),
        font="monospace",
        size=20,
    ):
        button = Button(text, text_color, bg_color, font, size)
        self.buttons[name] = button

    def draw_button(self, name, y, x="centre"):
        if x == "centre":
            self.buttons[name].rect.topleft = ((600 - self.buttons[name].width) / 2, y)
        else:
            self.buttons[name].rect.topleft = (x, y)
        self.screen.blit(
            self.buttons[name].image,
            (self.buttons[name].rect.x, self.buttons[name].rect.y),
        )

    def initialise_buttons(self):
        self.create_button("start", "START")
        self.create_button("resume", "RESUME")
        self.create_button("quit", "QUIT")
        self.create_button("play_again", "PLAY AGAIN")
        self.create_button("home", "HOME", size=15)
        self.create_button("continue", "CONTINUE")

    def display_start_screen(self):
        self.display_image("Graphics/title_screen.png", 0, 0)
        self.draw_button("start", 176)
        self.draw_button("resume", 225)
        self.draw_button("quit", 274)

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
        self.draw_button("continue", 340, 448)

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

        self.draw_button("play_again", 176)
        self.draw_button("quit", 225)

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
