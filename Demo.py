import pygame,sys, os
from random import randint

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
        self.images = {"theme": pygame.image.load("images/theme.png"), # 1792*1024
                        "front_door_lucky": pygame.image.load("images/front_door.jpg"), # 1024*1024
                        "front_door_unlucky": pygame.image.load("images/front_door_cat.jpg"), # 1024*1024
                        "backdoor.jpg" : pygame.image.load("images/back_door.jpg"), 
                        "backdoor_tripped" : pygame.image.load("images/backdoor_tripped.jpg"),
                        "catchtrain.jpg" : pygame.image.load("images/catchtrain.jpg"),
                        "catchtrain_spill.jpg" : pygame.image.load("images/catchtrain_spill.jpg"),
                        "crocs.jpg" : pygame.image.load("images/crocs.jpg"),
                        "jumpover.png" : pygame.image.load("images/jumpover.png"),
                        "jumpover_drenched.jpg" : pygame.image.load("images/jumpover_drenched.jpg"),
                        "waittrain_late.jpg" : pygame.image.load("images/waittrain_late.jpg"),
                        "waittrain_spill.jpg" : pygame.image.load("images/waittrain_spill.jpg"),
                        "walkthrough.jpg" : pygame.image.load("images/walkthrough.jpg")

                        }

        self.buttons = {
            "general": {"continue": Button("Continue", (255, 255, 255), (0, 128, 255), 50, 200),
                        "quit": Button("Quit", (255, 255, 255), (0, 128, 255), 50, 200),
                        "back" : Button("Back", (255, 255, 255), (0, 128, 255), 50, 200)},
            "menu": {"start_game": Button("Start Game", (255, 255, 255), (0, 128, 255), 50, 200),
                    "quit_game": Button("Quit Game", (255, 255, 255), (0, 128, 255), 50, 200)},
            "senario_door": {"front_door": Button("1. The Front Door!", (255, 255, 255), (0, 128, 255), 50, 200),
                          "back_door": Button("2. The Back Door!", (255, 255, 255), (0, 128, 255), 50, 200),
        }}
        self.last_change = 0
        

    def luck_change(self):
        self.changes = [-5, 5]
        self.last_change = self.changes[randint(0, 1)]
        return self.last_change

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
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
                        self.luck += self.luck_change()
                        self.state = 'back_door'
                elif self.state == 'front_door' or self.state == 'back_door':
                    if self.buttons['general']['continue'].is_clicked(event, event.pos):
                        self.state = 'ending'
                elif self.state == 'ending':
                    if self.buttons['general']['continue'].is_clicked(event, event.pos):
                        self.state = 'menu'
                    elif self.buttons['general']['quit'].is_clicked(event, event.pos):
                        sys.exit()
                    

    def display_button(self, button, position_x: int, position_y: int) -> None:
        button.rect.topleft = (position_x, position_y)
        self.screen.blit(button.surface, button.rect.topleft)

    def run(self):
        while True:
            self.screen.fill("WHITE")
            self.event_handler()

            if self.state == 'menu':
                self.screen.blit(pygame.transform.scale(self.images["theme"], (1280,720)), (0, 0))
                self.render_text = self.font.render("Welcom to LUCKOMETER", True, "BLACK")
                self.text_rect = self.render_text.get_rect()
                self.text_rect.center = (self.screen.get_width() // 2, 50)
                self.screen.blit(self.render_text, self.text_rect)
                self.display_button(self.buttons['menu']['start_game'], 300, 275)
                self.display_button(self.buttons['menu']['quit_game'], 300, 325)
            
            elif self.state == 'senario_door':
                self.screen.blit(pygame.transform.scale(self.images["theme"], (1280,720)), (0, 0))
                self.render_text = self.font.render("Let's get to work! Which door?", True, "BLACK")
                self.text_rect = self.render_text.get_rect()
                self.text_rect.center = (self.screen.get_width() // 2, 50)
                self.screen.blit(self.render_text, self.text_rect)
                self.display_button(self.buttons['senario_door']['front_door'], 300, 275)
                self.display_button(self.buttons['senario_door']['back_door'], 300, 325)
            
            elif self.state == 'front_door':
                if self.last_change > 0:
                    self.screen.blit(pygame.transform.scale(self.images["front_door_lucky"], (400,400)), (200, 160))
                    self.render_text = self.font.render("Cat is away!", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 700, 600)
                else:
                    self.screen.blit(pygame.transform.scale(self.images["front_door_unlucky"], (400,400)), (200, 160))
                    self.render_text = self.font.render("Cat is here!", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 700, 600)
            
            elif self.state == 'back_door':
                if self.last_change > 0:
                    self.screen.blit(pygame.transform.scale(self.images["backdoor_unlucky"], (400,400)), (200, 160))
                    self.render_text = self.font.render("Backdoor Lucky!", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 700, 600)
                else:
                    self.screen.blit(pygame.transform.scale(self.images["backdoor_tripped"], (400,400)), (200, 160))
                    self.render_text = self.font.render("Backdoor tripped!", True, "BLACK")
                    self.display_button(self.buttons['general']['continue'], 700, 600)

            elif self.state == "ending":
                self.screen.fill((0, 0, 0))
                self.render_text = self.font.render("Let's call this a day, your final lucky point is {self.luck}.", True, "BLACK")
                self.text_rect = self.render_text.get_rect()
                self.text_rect.center = (self.screen.get_width() // 2, 50)
                self.screen.blit(self.render_text, self.text_rect)
                self.display_button(self.buttons['general']['continue'], 300, 325)
                self.display_button(self.buttons['general']['quit'], 300, 375)

                    
                

            pygame.display.flip()
            self.clock.tick(60)

game = Game()
game.run()
