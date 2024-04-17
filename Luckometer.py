import pygame
import button  # this is a class i created, make sure you have it in your file to run the game
from random import randint, choice
from sys import exit

class Screen:
    def __init__(self, image, buttons=None, text=None):
        self.image = image
        self.buttons = buttons
        self.text = text

    # def add_buttons(self, file_loc: str, x, y, scale):
    #     button_img = pygame.image.load(f'{file_loc}').convert_alpha()
    #     new_button = button.Button(x, y, button_img, scale)
    #     self.buttons.append(new_button)
    def display(self):
        screen.blit(self.image, (0, 0))
        if self.buttons:
            for button in self.buttons:
              button.draw(screen)
        if self.text:
            screen.blit(self.text, (10, 10))


class Scenario:
    def __init__(self, scenario_num):
        self.screen = pygame.image.load(f'Graphics/scenario{scenario_num}.png').convert()
        self.c1_img = pygame.image.load(f'Graphics/s{scenario_num}_c1.png').convert_alpha()
        self.c2_img = pygame.image.load(f'Graphics/s{scenario_num}_c2.png').convert_alpha()
        self.c1_button = button.Button(293, 166, self.c1_img, 1)
        self.c2_button = button.Button(293, 246, self.c2_img, 1)
        self.cases = {}

    def set_case(self, choice, pos_outcome, neg_outcome):
        self.cases[choice] = [pos_outcome, neg_outcome]


# initialize pygame window
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Luckometer')
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 12)

# start screen elements
title_screen = pygame.image.load('Graphics/title_screen.png').convert()
start_img = pygame.image.load('Graphics/start_button.png').convert_alpha()
continue_img = pygame.image.load('Graphics/continue_button.png').convert_alpha()
quit_img = pygame.image.load('Graphics/quit_button.png').convert_alpha()

start_button = button.Button(233, 177, start_img, 1)
continue_button = button.Button(204, 234, continue_img, 1)
quit_button = button.Button(233, 291, quit_img, 1)

start_screen_buttons = [start_button, continue_button, quit_button]
start_screen = Screen(title_screen, start_screen_buttons)

# instruction screen
instruction_bg = pygame.image.load('Graphics/instructions.png').convert()
menu_img = pygame.image.load('Graphics/menu_button.png').convert_alpha()

menu_button = button.Button(503, 7, menu_img, 1)

instruction_screen = Screen(instruction_bg, [menu_button])

# scenario 1 outcomes
s1_c1_pos = pygame.image.load('Graphics/s1_c1_pos.png').convert()
s1_c1_neg = pygame.image.load('Graphics/s1_c1_neg.png').convert()
s1_c2_pos = pygame.image.load('Graphics/s1_c2_pos.png').convert()
s1_c2_neg = pygame.image.load('Graphics/s1_c2_neg.png').convert()

# Set scenario
s1 = Scenario(1)
s1.set_case('s1_c1', s1_c1_pos, s1_c1_neg)
s1.set_case('s1_c2', s1_c2_pos, s1_c2_neg)

# scenario 1 elements
luck_score = randint(-50, 50)
luck_score_surface = font.render(f'Luck Score: {luck_score}', True, 'black')

screen_s1 = Screen(s1.screen, [menu_button, s1.c1_button, s1.c2_button], luck_score_surface)


def run_game():
    global luck_score
    global luck_score_surface

    current_screen = start_screen  # Initial screen is the start screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if current_screen == instruction_screen:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    current_screen = screen_s1

        if current_screen == start_screen:
            if start_button.get_clicked():
                current_screen = instruction_screen
            if continue_button.get_clicked():
                print("CONTINUE")
            if quit_button.get_clicked():
                pygame.quit()
                exit()

        if menu_button.get_clicked():
            current_screen = start_screen

        if current_screen == screen_s1:
            if s1.c1_button.get_clicked():
                outcome = choice(s1.cases['s1_c1'])
                if outcome == s1_c1_pos:
                    luck_score += 5
                if outcome == s1_c1_neg:
                    luck_score -= 5
                luck_score_surface = font.render(f'Luck Score: {luck_score}', True, 'black')
                current_screen = Screen(outcome, [menu_button], luck_score_surface)
            if s1.c2_button.get_clicked():
                outcome = choice(s1.cases['s1_c2'])
                if outcome == s1_c2_pos:
                    luck_score += 5
                if outcome == s1_c2_neg:
                    luck_score -= 5
                luck_score_surface = font.render(f'Luck Score: {luck_score}', True, 'black')
                current_screen = Screen(outcome, [menu_button], luck_score_surface)

        screen.fill('black')
        current_screen.display()

        pygame.display.update()
        clock.tick(60)

run_game()
