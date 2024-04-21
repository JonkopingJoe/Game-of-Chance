import pygame
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
            print("An error occurred while creating a node, please check the input values!", e)


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
            print("An error occurred while appending a node, please check the input values!", e)

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
            print("An error occurred while converting the linked list to a list, please check the input values!", e)

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
            print("An error occurred while traversing the linked list, please check the input values!", e)


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
        self.luck_score = 100
        self.scenarios_Linked_list = None
        self.current_state = None
        self.initialize_game_scenarios_list()
        self.buttons = {}
        self.initialise_buttons()
        self.current_screen = ''
        self.log = open('luckometer.log', 'w') # Event Logging File

    # Displaying Section
    def display_text(self,
                     text: str,
                     text_color: tuple,
                     bg_color=None,
                     x='centre',
                     y='centre',
                     font='comic sans',
                     size=FONT_SIZE
    ) -> None:
        font = pygame.font.SysFont(font, size)
        lines = text.split('\n')
        line_surfaces = [font.render(line, False, text_color, bg_color) for line in lines]

        if x == 'centre' and y == 'centre':
            # Calculating the x and y coordinates to center the instruction on the screen with padding
            x = (screen_width - max(line_surface.get_width() for line_surface in line_surfaces)) / 2
            y = (screen_height - sum(line_surface.get_height() for line_surface in line_surfaces)) / 2

        # Finally blitting each line to the screen
        for i, line_surface in enumerate(line_surfaces):
            self.screen.blit(line_surface, (x, y + i * (line_surface.get_height())))

        return None

    def display_scenario(self, scenario: Scenario) -> None:
        # button1 = Button(scenario.cases["choice1"], (167, 66, 132), WHITE)
        # button2 = Button(scenario.cases["choice2"], (167, 66, 132), WHITE)
        # self.display_button(button1, 400, 300)
        # self.display_button(button2, 400, 325)
        self.create_button('s1_choice1', scenario.cases['choice1'])
        self.create_button('s1_choice2', scenario.cases['choice2'])
        self.screen.fill('white')
        self.display_text(scenario.caption, BLACK, x=45, y=30, size=20)
        self.display_image(scenario.picture_path, 25, 137)
        self.draw_button('s1_choice1', 186, 320)
        self.draw_button('s1_choice2', 246, 320)

        self.log_event(f'{scenario} displayed')
        self.current_screen = f'{scenario}'

    def display_button(self, button: Button, x: int, y: int) -> None:
        button.text_rect.center = (x, y)
        self.screen.blit(button.render_text, button.text_rect)
        return None

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

            '''The Day Begins.
            Let’s get you to work! 
            Which door are you leaving your house through?''',

            # First
            "The Front Door",
            "Yay! That stray cat that always gouges\nyour eyes out is nowhere in sight!\n\nLuck +5",
            "OW! That cat is here today, you just got scratched ;(\n\nLuck -5",
            # Second
            "The Back Door",
            "Phew, narrowly escaped that nosy neighbour!\n\nLuck +5",
            "Oh no, you tripped over that bucket of\nwater you left out last night!\n\nLuck -5"
        )

        # scenario two
        scenario2 = Scenario(2, "./waittrain_late_small.jpg")
        scenario2.set_cases(
            "random_caption",
            "wait for the train",
            "you catched the train",
            "the train was tirmminated",
            "skip the train and book an uber",
            "you skipped the train and the uber is too expensive",
            "the uber is cheaper",
        )

        # scenario three
        scenario3 = Scenario(3, "./waittrain_late_small.jpg")
        scenario3.set_cases(
            "random_caption",
            "wait for the train",
            "you catched the train",
            "the train was tirmminated",
            "skip the train and book an uber",
            "you skipped the train and the uber is too expensive",
            "the uber is cheaper",
        )

        # scenario four
        scenario4 = Scenario(4, "./waittrain_late_small.jpg")
        scenario4.set_cases(
            "random_caption",
            "wait for the train",
            "you catched the train",
            "the train was tirmminated",
            "skip the train and book an uber",
            "you skipped the train and the uber is too expensive",
            "the uber is cheaper",
        )

        self.scenarios_Linked_list = get_game_scenarios([scenario1, scenario2, scenario3, scenario4])

        return self.scenarios_Linked_list

    def main_menu(self) -> None:
        self.display_image("pictures/game_background.png")

    # Luck Changing function
    def random_luck_diff(self) -> int:
        # return the change in luck
        return randint(-10, 10)

    def log_event(self, event):
        """Logs events and the timestamp when they occur."""
        timestamp = pygame.time.get_ticks()  # Gets the number of milliseconds since pygame.init() was called
        log_message = f'{timestamp/1000}s: {event}\n'
        self.log.write(log_message)
        print(log_message)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.log_event('QUIT CLICKED')
                pygame.quit()
                self.log.close()
                exit()

            if self.current_screen in ('start', 'end'):
                if self.buttons['quit'].is_clicked():
                    self.log_event('QUIT BUTTON CLICKED')
                    pygame.quit()
                    self.log.close()
                    exit()

            if self.current_screen == 'start':
                if self.buttons['start'].is_clicked():
                    self.log_event('START BUTTON CLICKED')
                    self.display_instructions_screen()

                if self.buttons['resume'].is_clicked():
                    self.log_event('RESUME BUTTON CLICKED')

            if self.current_screen == 'instruction':
                if self.buttons['menu'].is_clicked():
                    self.log_event('MENU BUTTON CLICKED')
                    self.display_start_screen()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.log_event('SPACEBAR BUTTON PRESSED')
                    if self.scenarios_Linked_list and self.scenarios_Linked_list.head:
                        self.current_state = self.scenarios_Linked_list.head.value
                        self.display_scenario(self.current_state)

            if self.current_screen == 'scenario1':
                if self.buttons['s1_choice1'].is_clicked():
                    self.display_outcome(1)
                if self.buttons['s1_choice2'].is_clicked():
                    self.display_outcome(2)
                if self.buttons['continue'].is_clicked():
                    self.current_state = self.scenarios_Linked_list.head.next.value
                    self.display_scenario(self.current_state)

            if self.current_screen == 'end':
                if self.buttons['play_again'].is_clicked():
                    self.log_event('PLAY AGAIN BUTTON CLICKED')
                    self.display_start_screen()

    def create_button(
            self,
            name: str,
            text: str,
            text_color=(167, 66, 132),
            bg_color=(221, 229, 13),
            font='monospace',
            size=20
    ):
        button = Button(text, text_color, bg_color, font, size)
        self.buttons[name] = button

    def draw_button(self, name, y, x='centre'):
        if x == 'centre':
            self.buttons[name].rect.topleft = ((600 - self.buttons[name].width)/2, y)
        else:
            self.buttons[name].rect.topleft = (x, y)
        self.screen.blit(self.buttons[name].image, (self.buttons[name].rect.x, self.buttons[name].rect.y))

    def initialise_buttons(self):
        self.create_button('start', 'START')
        self.create_button('resume', 'RESUME')
        self.create_button('quit', 'QUIT')
        self.create_button('play_again', 'PLAY AGAIN')
        self.create_button('menu', 'MENU', size=15)
        self.create_button('continue', 'CONTINUE')

    def display_start_screen(self):
        screen = pygame.image.load('Graphics/title_screen.png').convert()
        self.screen.blit(screen, (0, 0))
        self.draw_button('start', 176)
        self.draw_button('resume', 225)
        self.draw_button('quit', 274)

        self.log_event('START SCREEN DISPLAYED')
        self.current_screen = 'start'

    def display_instructions_screen(self):
        screen = pygame.image.load('Graphics/instructions.png').convert()
        self.screen.blit(screen, (0, 0))
        self.draw_button('menu', 10, 530)

        # Defining the instructions text
        instruction = '''
        The game starts at home, and the day begins. 
        You start off with a randomised luck score, 
        and each decision you make will have an effect.
        Remember, this is a game of luck, so no matter how sound
        your choice may seem, there is always a twist. 
        Your aim is to have the highest luck at the end of the game. 
        Good Luck!
        '''

        self.display_text(instruction, WHITE, size=17)
        self.log_event('INSTRUCTIONS SCREEN DISPLAYED')
        self.current_screen = 'instruction'

    def display_outcome(self, choice_num):
        outcomes = [self.scenarios_Linked_list.head.value.cases[f'pos_outcome{choice_num}'],
                    self.scenarios_Linked_list.head.value.cases[f'neg_outcome{choice_num}']]
        outcome = choice(outcomes)
        self.screen.fill(WHITE)
        self.display_text(outcome, BLACK, size=20)
        self.draw_button('continue', 340, 448)

    def display_end_screen(self):
        screen = pygame.image.load('Graphics/end_screen.png').convert()
        self.screen.blit(screen, (0, 0))
        self.display_text(f'Your Final Luck Score is {self.luck_score}. What a day!', (0, 0, 0,), (255, 255, 255), 88, 100, font_size=20)
        self.draw_button('play_again', 176)
        self.draw_button('quit', 225)

        self.log_event('END SCREEN DISPLAYED')
        self.current_screen = 'end'

    def get_text_rect(self, text, x, y) -> tuple:
        rendered_text = self.font.render(text, True, (255, 255, 255))
        text_rect = rendered_text.get_rect(center=(x, y))
        return rendered_text, text_rect

    def run(self):
        self.screen.fill((0, 0, 0))
        self.current_screen = 'start'
        self.display_start_screen()

        while True:
            self.handle_events()
            pygame.display.flip()
            self.clock.tick(60)


game = Game()
game.run()
