import pygame, sys, os

pygame.init()


class GameState:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() 
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("LUCKOMETER: TWISTED FATE")
        self.clock = pygame.time.Clock()
        self.font.SysFont("Aptos", 45)

    def load_sound(self, name: str):
        # if not pygame.mixer or not pygame.mixer.get_init():
        #     return NoneSound()

        fullname = os.path.join(r"path", name)
        sound = pygame.mixer.Sound(fullname)
        return sound
    
    def load_image(self, name, colorkey=None, scale=1):
        fullname = os.path.join(r"path", name)
        image = pygame.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pygame.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey ==- -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    def draw_text(self, text, color, position):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def create_button(self, text, position, base_color, hovering_color):
        text_surface = self.font.render(text, True, base_color)
        button_rect = text_surface.get_rect(center=position)
        return text_surface, button_rect, base_color, hovering_color

    def check_for_input(self, button_rect, position):
        return button_rect.collidepoint(position)

    def change_color(self, text_surface, base_color, hovering_color, position):
        if text_surface.get_rect(center=position).collidepoint(position):
            return pygame.font.SysFont("Aptos", 45).render(text_surface.get_text(), True, hovering_color)
        else:
            return pygame.font.SysFont("Aptos", 45).render(text_surface.get_text(), True, base_color)
   
