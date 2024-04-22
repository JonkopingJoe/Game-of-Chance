import pygame
from random import choice
from scenario import Scenario
from button import Button
from scenarios_tree import get_game_scenarios
# from linkedlist import LinkedList
from linkedlist import Linkedlist
from sys import exit


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
FONT_SIZE = 12

class Game:
    def __init__(self):

        # WINDOW AND BUTTONS SET UP
        pygame.init()
        pygame.display.set_caption("LUCKOMETER")
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", FONT_SIZE)
        self.luck_score = 100
        self.game_scenarios = get_game_scenarios() 
        self.buttons = {}
        self.initialise_buttons()


        self.state = "start"
        self.events_log = open('luckometer_log.txt', 'w')
        self.current_screen = None

    # BUTTONS SECTINO

    def create_button(self, name: str, text: str, text_color=(167, 66, 132), bg_color=(221, 229, 13), font='monospace', size=20):
        button = Button(text, text_color, bg_color, font, size)
        self.buttons[name] = button

    def draw_button(self, name, y, x='centre'):
        if x == 'centre':
            self.buttons[name].rect.topleft = ((600 - self.buttons[name].width)/2, y)
        else:
            self.buttons[name].rect.topleft = (x, y)
        self.screen.blit(self.buttons[name].image, (self.buttons[name].rect.x, self.buttons[name].rect.y))
    
    def initialise_buttons(self):
        self.create_button("start", "START")
        self.create_button("quit", "QUIT")
        self.create_button("play_again", "PLAY AGAIN")


        # All the scenarios buttons
        game_scenarios_linkedlist = self.game_scenarios.copy() 
        current_Linkedlist_node = game_scenarios_linkedlist.head

        count = 1
        while(current_Linkedlist_node):
            current_scenarios = current_Linkedlist_node.data

            self.create_button(f"scenario{count}_choice1", current_scenarios.cases["choice1"])
            self.create_button(f"scenario{count}_choice2", current_scenarios.cases["choice2"])

            current_Linkedlist_node = current_Linkedlist_node.next
            count += 1

    # DISPLAYING SECTION

    def display_text(self, text: str, text_color: tuple, bg_color: tuple, x: int, y: int, font_size=FONT_SIZE) -> None:
        displaying_font = self.font

        if font_size != FONT_SIZE:
            displaying_font = pygame.font.SysFont("monospace", font_size)

        render_text = displaying_font.render(text, True, text_color, bg_color)
        self.screen.blit(render_text, (x, y))

        return None

    def display_scenario(self, scenario: Scenario, scenario_number: int) -> None:
        self.screen.fill(WHITE)
        self.display_text(scenario.caption, BLACK, WHITE, 10, 10)
        try: 
            self.display_image(scenario.picture_path, 25, 70)
        except: 
            self.display_image("Graphics/back_door_safe.png", 25, 50)

        self.draw_button(f"scenario{scenario_number}_choice1", 180, 300)
        self.draw_button(f"scenario{scenario_number}_choice2", 220, 300)
    

    def run_scenario(self, scenario: Scenario, scenario_number: int) -> bool:
        if self.buttons[f"scenario{scenario_number}_choice1"].is_clicked(): 
            pass 


    def display_image(self, image_path: str, x: int, y: int) -> None:
        img = pygame.image.load(image_path).convert()
        self.screen.blit(img, (x, y))
        return None

    def display_start_screen(self):
        print('start display')
        self.display_image('Graphics/title_screen.png', 0, 0)
        self.draw_button('start', 176)
        self.draw_button('quit', 227)

    def display_instructions_screen(self):
        self.current_screen = 'instruction'
        print('instruction display')
        instructions_bg = pygame.image.load(
            'Graphics/instructions.png').convert()
        self.screen.blit(instructions_bg, (0, 0))
        # self.draw_button('menu', 10, 530)

        # Get the screen width and height
        screen_width, screen_height = self.screen.get_size()

        # Defining the instructions text
        instruction = 'The game starts at home, and the day begins. You start off with' \
            + '\na randomised luck score, and each decision you make will have an effect.' \
            + '\nRemember, this is a game of luck, so no matter how sound' \
            + '\nyour choice may seem, there is always a twist. Your aim is to have the' \
            + '\nhighest luck at the end of the game. Good Luck!'

        # Then rendering each line of the paragraph separately using list comprehension
        # None for default font if Comic Sans is not found in the system
        font = pygame.font.SysFont('comic sans', 16, True)
        lines = instruction.split('\n')
        line_surfaces = [font.render(line, False, WHITE) for line in lines]

        # Calculating the x and y coordinates to center the instruction on the screen with padding
        x = (screen_width - max(line_surface.get_width()
             for line_surface in line_surfaces)) / 2 + 9
        y = (screen_height - sum(line_surface.get_height()
             for line_surface in line_surfaces)) / 2 - 9

        # Finally blitting each line to the screen
        for i, line_surface in enumerate(line_surfaces):
            self.screen.blit(
                line_surface, (x, y + i * (line_surface.get_height()+10)))

    def display_end_screen(self):
        screen = pygame.image.load('Graphics/end_screen.png').convert()
        self.screen.blit(screen, (0, 0))
        self.display_text(
            f'Your Final Luck Score is {self.luck_score}. What a day!', BLACK, YELLOW, 70, 100, font_size=20)
        self.draw_button('play_again', 176)
        self.draw_button('quit', 225)

    # HANDLING EVETNS

    def handle_events(self):
        log_events = lambda event: self.events_log.write(f"{event}\n")
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (self.current_screen in ('start', 'end') and self.buttons['quit'].is_clicked()):
                log_events('QUIT CLICKED')
                self.events_log.close()
                pygame.quit()
                exit()

            # if self.buttons['menu'].is_clicked():
            #     self.current_screen = 'start'
            #     self.display_start_screen()
            #     log_events('MENU CLICKED')

            if self.current_screen == 'start':
                if self.buttons['start'].is_clicked():
                    self.current_screen = 'instruction'
                    self.display_instructions_screen()
                    log_events('START CLICKED')

            if self.current_screen == 'instruction':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # self.display_scenarios()
                    # self.current_screen = 'end'
                    # self.display_end_screen()
                    log_events('INSTRUCTIONS PASSED')
                    self.current_screen = "scenario"

            
            if self.current_screen == "scenario": 

                game_scenarios_linkedlist = self.game_scenarios.copy() 
                current_Linkedlist_node = game_scenarios_linkedlist.head 
                count = 1

                self.display_scenario(current_Linkedlist_node.data, 1)

                # while(current_Linkedlist_node):
                #     current_scenario = current_Linkedlist_node.data

                #     self.display_scenario(current_scenario, count)

                #     current_Linkedlist_node = current_Linkedlist_node.next
                #     count += 1

                

        

            if self.current_screen == 'end':
                if self.buttons['play_again'].is_clicked():
                    self.current_screen = 'start'
                    self.display_start_screen()
                    log_events('PLAY AGAIN CLICKED')


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
