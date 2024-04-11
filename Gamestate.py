import pygame, sys, os

pygame.init()

class Button:
    def __init__(self, text, position, font, base_color, hovering_color):
        self.text = text
        self.position = position
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.rect = self.font.render(self.text, True, self.base_color).get_rect(center = self.position)

    def update(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            text_surface = self.font.render(self.text, True, self.hovering_color)
        else:
            text_surface = self.font.render(self.text, True, self.base_color)
        screen.blit(text_surface, self.rect)
class GameState:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() 
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("LUCKOMETER: TWISTED FATE")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Aptos", 45)

    def load_sound(self, name: str):
        # if not pygame.mixer or not pygame.mixer.get_init():
        #     return NoneSound()

        fullname = os.path.join(r"path", name)
        sound = pygame.mixer.Sound(fullname)
        return sound
    
    def load_image(self, name, colorkey = None, scale = 1):
        fullname = os.path.join(r"path", name)
        image = pygame.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pygame.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    def draw_text(self, text, color, position):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center = position)
        self.screen.blit(text_surface, text_rect)

    def main_menu(self): # formerly MainMenu Class
        play_button = Button("PLAY", (640, 200), self.font, "black", (0, 255, 0))
        continue_button = Button("CONTINUE", (640, 300), self.font, "black", (0, 255, 0))
        instructions_button = Button("HOW TO PLAY", (640, 400), self.font, "black", (0, 255, 0))
        quit_button = Button("QUIT",(640, 500), self.font, "black", (255, 0, 0))

        while True:
            self.screen.fill((255, 255, 255)) # TO DO: blit() rather than fill()
            self.draw_text("LUCKOMETER: TWISTED FATE", (0, 0, 0), (640, 100))

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.rect.collidepoint(mouse_pos):
                        self.play()
                    elif continue_button.rect.collidepoint(mouse_pos):
                        self.continue_()
                    elif instructions_button.rect.collidepoint(mouse_pos):
                        self.instructions() # TO DO: add a listen event rather than wait()
                    elif quit_button.rect.collidepoint(mouse_pos):
                        self.quit()

            play_button.update(self.screen, mouse_pos)
            continue_button.update(self.screen, mouse_pos)
            instructions_button.update(self.screen, mouse_pos)
            quit_button.update(self.screen, mouse_pos)

            pygame.display.flip()
            self.clock.tick(60)

    def play(self):
        # placeholder for play event 
        # event will lead to a random scenario
        pass

    def instructions(self):
        self.screen.fill((255, 255, 0))
        instruction = """This is how to play the game:

        1.Imagine that you are starting your day,
        2.You get to choose what you'd rather do
        3.Each choice shall lead to the next
        4.For each progress, you will either be 'Lucky' and add points
        5.Or 'Unlucky' and lose point. You're literally trying your luck
        6.Aim is not to end up with the most luck"""

        # Adjusting font size to fit within the screen
        font_size = 30
        font = pygame.font.SysFont(None, font_size)
        text_color = (0, 0, 0)

        # Splitting multiline text into individual lines
        lines = instruction.split("\n")
        y_pos = 100

        # Rendering and displaying each line of text
        for line in lines:
            text_surface = font.render(line.strip(), True, text_color)
            text_rect = text_surface.get_rect(center=(640, y_pos))
            self.screen.blit(text_surface, text_rect)
            y_pos += font_size  # Adjusting vertical position for next line

        pygame.display.flip()
        pygame.time.wait(2000)

    def continue_(self):
        # placeholder for continue event
        # will open to a random scenario
        pass

    def quit(self):
        pygame.quit()

# Test window to view what to correct
if __name__ == "__main__":
    game = GameState()
    game.main_menu()
