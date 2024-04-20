import pygame
from random import randint, choice
from scenario import Scenario
from button import Button
from linked_list import LinkedList, ListNode, get_game_scenarios

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
FONT_SIZE = 12

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LUCKOMETER")
        self.state = "menu"
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", FONT_SIZE)
        self.luck_score = 100
        self.scenarios_list = self.initialize_game_scenarios_list()
        self.buttons = {}
        self.initialise_buttons()
        self.current_screen = ''
    # Displaying Seciton
    def display_text(self, text: str, text_color: tuple, bg_color: tuple, x: int, y: int, font_size=FONT_SIZE) -> None: 
        displaying_font = self.font

        if font_size != FONT_SIZE: 
            displaying_font = pygame.font.SysFont("monospace", font_size)


        render_text = displaying_font.render(text, True, text_color, bg_color)
        self.screen.blit(render_text, (x, y))

        return None
    def display_scenario(self, scenario: Scenario) -> None: 
        button1 = Button(scenario.cases["choice1"], BLACK, WHITE)
        button2 = Button(scenario.cases["choice2"], BLACK, WHITE)

        self.display_text(scenario.caption, BLACK, WHITE, 100, 100)
        self.display_image(scenario.picture_path, 25, 137)
        self.display_button(button1, 100, 125)
        self.display_button(button2, 100, 135)
        

    def display_button(self, button: Button, x: int, y: int) -> None:
        button.text_rect.center = (x, y)
        self.screen.blit(button.render_text, button.text_rect)

        return None

    def display_image(self, image_path: str, x: int, y: int) -> None:
        img = pygame.image.load(image_path).convert()
        self.screen.blit(img, (x, y))
        return None


    def initialize_game_scenarios_list(self) -> list:
        scenarios_list = []

        # scenario one
        train_watting = Scenario("./waittrain_late_small.jpg")
        train_watting.set_cases(

            "random_caption"

            # First
            "wait for the train",
            "you catched the train",
            "the train was tirmminated",
            ## Second
            "skip the train and book an uber",
            "you skipped the train and the uber is too expensive",
            "the uber is cheaper",
            "one extra"
        )

        # appending scenario

        return scenarios_list

    def get_scenarios_flow(self) -> LinkedList:
        scenario_flow_linkedList = LinkedList()

        while (
            len(scenario_flow_linkedList) < 4
        ):  # The full game loop is made of four scenarios.
            random_scenario = choice(self.scenarios_list())

            if random_scenario not in scenario_flow_linkedList:
                scenario_flow_linkedList.append(random_scenario)

        return scenario_flow_linkedList


    def main_menu(self) -> None:
        self.display_image("pictures/game_background.png")

    # Luck Changing function
    def random_luck_diff(self) -> int:
        # return the change in luck
        return randint(-10, 10)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.current_screen == 'start':
                if self.buttons['start'].is_clicked():
                    print('START')
                    self.display_instructions_screen()

                if self.buttons['resume'].is_clicked():
                    print('RESUME')

                if self.buttons['quit'].is_clicked():
                    pygame.quit()
                    exit()

            if self.current_screen == 'menu':
                if self.buttons['menu'].is_clicked():
                    self.display_start_screen()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.display_end_screen()

            if self.current_screen == 'end':
                if self.buttons['play_again'].is_clicked():
                    print('PLAY AGAIN')
                    self.display_start_screen()

                if self.buttons['quit'].is_clicked():
                    pygame.quit()
                    exit()

    def create_button(self, name: str, text, text_color=(167, 66, 132), bg_color=(221, 229, 13), font='monospace', size=20):
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

    def display_start_screen(self):
        print('start display')
        self.current_screen = 'start'
        screen = pygame.image.load('Graphics/title_screen.png').convert()
        self.screen.blit(screen, (0, 0))
        self.draw_button('start', 176)
        self.draw_button('resume', 225)
        self.draw_button('quit', 274)

    def display_instructions_screen(self):
        self.current_screen = 'menu'
        screen = pygame.image.load('Graphics/instructions.png').convert()
        self.screen.blit(screen, (0, 0))
        self.draw_button('menu', 10, 530)

    def display_end_screen(self):
        print('end display')
        self.current_screen = 'end'
        screen = pygame.image.load('Graphics/end_screen.png').convert()
        self.screen.blit(screen, (0, 0))
        self.display_text(f'Your Final Luck Score is {self.luck_score}. What a day!', (0, 0, 0,), (255, 255, 255), 88, 100, font_size=20)
        self.draw_button('play_again', 176)
        self.draw_button('quit', 225)

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