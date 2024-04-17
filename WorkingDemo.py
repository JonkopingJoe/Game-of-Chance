# WorkingDemo
import pygame, sys, os
from random import randint


# class Demo:
#     def __init__(self):
#         pygame.init()
#         self.state = 'menu'
#         self.screen = pygame.display.set_mode((1280, 720))
#         pygame.display.set_caption("LUCKOMETER")
#         self.clock = pygame.time.Clock()
#         self.font = pygame.font.Font(None, 36)
#         self.luck = 100
#         # Need a better way to load background images, may be a dictionary
#         self.city = pygame.image.load('graphics/City_Background.webp').convert_alpha()
#         self.pond_background = pygame.image.load('graphics/pond.webp').convert_alpha()
#         self.menu_options = {}
#         self.game_options = {}
#         self.last_change = 0

#     def display_surface(self, text, x, y):
#         text_surface = self.font.render(text, True, (255, 255, 255))
#         text_rect = text_surface.get_rect(center=(x, y))
#         self.screen.blit(text_surface, text_rect)
#         return text_surface, text_rect

#     def display_background(self, background):
#     # Display background image
#     #!!! Need to be reconstructed to receive path, position and size, may be integrated with display_surface
#         self.screen.blit(background, (0, 0))

#     def display_text(self, text, x, y):
#         rendered_text = self.font.render(text, True, (255, 255, 255))
#         text_pos = rendered_text.get_rect(center=(x, y))
#         self.screen.blit(rendered_text, text_pos)
#         return text_pos

#     def handle_events(self):
#     # Display luck on the screen
#     #!!! Need to be reconstructed to show an ometer
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
#                 if self.state == 'menu':
#                     if self.menu_options['start_game'].collidepoint(event.pos):
#                         self.state = 'game'
#                         self.create_game_options()
#                     elif self.menu_options['quit_game'].collidepoint(event.pos):
#                         sys.exit()
#                 elif self.state == 'game':
#                     for option, rect in self.game_options.items():
#                         if rect.collidepoint(event.pos):
#                             change = self.process_event()
#                             self.luck += change
#                             self.last_change = change
#                             self.state = 'event_end'
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                 if self.state == 'event_end':
#                     self.state = 'end'
#                 elif self.state == 'end':
#                     self.luck = 100
#                     self.state = 'menu'

#     def process_event(self):
#         # return the change in luck
#         return randint(-10, 10)


#     def display_luck(self):
#     # Display luck on the screen
#     #!!! Need to be reconstructed to show an ometer
#         luck_text = f"Luck: {self.luck}"
#         self.display_text(luck_text, self.screen.get_width()/2, 50)

#     def show_menu(self):
#     # Display menu
#     #!!! May integrate with a background image
#         self.menu_options['start_game'] = self.display_text("Start Game", self.screen.get_width()/2, 300)
#         self.menu_options['quit_game'] = self.display_text("Quit Game", self.screen.get_width()/2, 350)

#     def create_game_options(self):
#     # Create game options
#     #!!! Need to be reconstructed to receive options as a list, to handle more events
#     # create_game_options(self, options_for_event: list)
#         self.game_options['option1'] = self.display_surface("1. Jump Over the Pond", self.screen.get_width()/2, 200)[1]
#         self.game_options['option2'] = self.display_surface("2. Walk Around the Pond", self.screen.get_width()/2, 250)[1]
#         self.game_options['option3'] = self.display_surface("3. Walk Through the Pond", self.screen.get_width()/2, 300)[1]


#     def run(self):
#     # !!!Could make it a independent class
#     # We may create an independent classes of game_state, and call them here
#         while True:
#             self.screen.fill((0, 0, 0))
#             self.handle_events()

#             # Integrate following block into class menu = GameState('menu')
#             if self.state == 'menu':
#                 self.display_background(self.city) # May be integrated with show_menu
#                 self.show_menu()
#             # Integrate following block into class game = GameState('game')
#             elif self.state == 'game':
#                 self.display_background(self.pond_background) # May be integrated with a new Event class
#                 self.display_luck()
#                 self.create_game_options()
#             # Integrate following block into class event = GameState('event')
#             elif self.state == 'event_end':
#                 self.screen.fill((0, 0, 0))
#                 change_text = f"Your lucky point changed {self.last_change:+d}."
#                 self.display_text(change_text, self.screen.get_width()/2, self.screen.get_height()/2 - 50)
#                 prompt_text = "Press SPACE to continue."
#                 self.display_text(prompt_text, self.screen.get_width()/2, self.screen.get_height()/2 + 50)
#             # Integrate following block into class end = GameState('end')
#             elif self.state == 'end':
#                 self.screen.fill((0, 0, 0))
#                 final_text = f"Let's call this a day, your final lucky point is {self.luck}."
#                 self.display_text(final_text, self.screen.get_width()/2, self.screen.get_height()/2 - 50)
#                 prompt_text = "Press SPACE to return to the main menu."
#                 self.display_text(prompt_text, self.screen.get_width()/2, self.screen.get_height()/2 + 50)
            
#             pygame.display.flip()
#             self.clock.tick(60)

# if __name__ == "__main__":
#     Demo().run()

class Button(pygame.sprite.Sprite):
    def __init__(self, text: str, text_color: tuple, bg_color: tuple, height: int, width: int):
        super().__init__()
        
        # Default font
        font = pygame.font.Font(None, 36)

        # Display surface
        self.surface = pygame.Surface([width, height])
        self.surface.fill(bg_color)

        # Render text and align
        self.render_text = font.render(text, True, text_color)
        self.text_rect = self.render_text.get_rect()
        
        # Calculate text position to center it
        self.text_rect.center = (width // 2, height // 2)
        
        # Draw text on the button's surface
        self.surface.blit(self.render_text, self.text_rect)
        
        # Store rect for position and collision detection
        self.rect = self.surface.get_rect()

    def is_clicked(self, event, pos) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False
    


class Game():
    def __init__(self):
        pygame.init()
        self.state = 'menu'
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("LUCKOMETER")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.luck = 100
        self.images = {}    
        self.buttons = {
            "general": {"continue": Button("Continue", (255, 255, 255), (0, 128, 255), 50, 200),
                        "back" : Button("Back", (255, 255, 255), (0, 128, 255), 50, 200)},
            "menu": {"start_game": Button("Start Game", (255, 255, 255), (0, 128, 255), 50, 200),
                    "quit_game": Button("Quit Game", (255, 255, 255), (0, 128, 255), 50, 200)},
            "senario_door": {"front_door": Button("  1.The Front Door!  ", (255, 255, 255), (0, 128, 255), 50, 200),
                          "back_door": Button("  2.The Back Door!  ", (255, 255, 255), (0, 128, 255), 50, 200),
        }}
        self.game_options = {}
        self.last_change = 0

    def load_images_scaled(self, folder_path, scale=1) -> dict:
        images = {}

        # screen dimensions
        screen_width = 1280 
        screen_height = 720

        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".webp")):
                filepath = os.path.join(folder_path, filename)
                try:
                    img_surface = pygame.image.load(filepath).convert_alpha()
                    original_size = img_surface.get_size()
                    # scale factor to fit the screen
                    scale_factor = min(screen_width / original_size[0], screen_height / original_size[1])
                    scaled_size = (int(original_size[0] * scale_factor * scale), int(original_size[1] * scale_factor * scale))
                    scaled_image = pygame.transform.scale(img_surface, scaled_size)
                    images[filename] = scaled_image
                    self.images[filename] = scaled_image
                except pygame.error as e:
                    print(f"Error loading or scaling image '{filename}': {e}")
        return images

    def load_sound(self, name: str):

        fullname = os.path.join(r"Game-of-Chance\audio", name)
        sound = pygame.mixer.Sound(fullname)
        return sound
    
    def luck_change(self):
        self.changes = [-5, 5]
        self.last_change = self.changes[randint(0, 1)]
        return self.last_change

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                if self.state == 'menu':
                    if self.buttons['menu']['start_game'].is_clicked(event, event.pos):
                        self.state = 'senario_door'
                    elif self.buttons['menu']['quit_game'].is_clicked(event, event.pos):
                        sys.exit()
                elif self.state == 'senario_door':
                    if self.buttons['senario_door']['front_door'].is_clicked(event, event.pos):
                        self.luck += self.luck_change()
                        self.state = 'front_door'
                    elif self.buttons['senario_door']['back_door'].is_clicked(event, event.pos):
                        self.state = 'back_door'
                    

    def display_button(self, button, positio_x: int, position_y: int) -> None:
        button.rect.topleft = (positio_x, position_y)
        self.screen.blit(button.surface, button.rect.topleft)

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.event_handler()
            # sound = self.load_sound("not-really-lost.wav")
            # sound.play()


            if self.state == 'menu':
                self.screen.blit((self.images["theme.png"]), (0, 0))
                self.render_text = self.font.render("Welcome to LUCKOMETER. Try to earn the most Luck!", True, "BLACK")
                self.text_rect = self.render_text.get_rect()
                self.text_rect.center = (self.screen.get_width() // 2, 50)
                self.screen.blit(self.render_text, self.text_rect)
                self.display_button(self.buttons['menu']['start_game'], 515, 275)
                self.display_button(self.buttons['menu']['quit_game'], 515, 375)
            
            elif self.state == 'senario_door':
                self.screen.blit(self.images["theme.png"], (0, 0))
                self.render_text = self.font.render("Let's get to work! Which door?", True, "BLACK")
                self.text_rect = self.render_text.get_rect()
                self.text_rect.center = (self.screen.get_width() // 2, 50)
                self.screen.blit(self.render_text, self.text_rect)
                self.display_button(self.buttons['senario_door']['front_door'], 515, 275)
                self.display_button(self.buttons['senario_door']['back_door'], 515, 375)
            
            elif self.state == 'front_door':
                if self.last_change > 0:
                    self.screen.blit(self.images["front_door.jpg"], (0, 0))
                    self.render_text = self.font.render("Cat is away! You Earned Luck", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 300, 325)
                else:
                    self.screen.blit(self.images["front_door_cat.jpg"], (0, 0))
                    self.render_text = self.font.render("Cat is here! Luck Deducted", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 300, 325)
                    
                

            pygame.display.flip()
            self.clock.tick(60)

game = Game()
print(game.load_images_scaled(r"Game-of-Chance\images")) # working : returns image name keys, and image surface values
game.run()


