import pygame 

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
font = pygame.font.SysFont("monospace", 12)


# Object class 
class Button(pygame.sprite.Sprite): 
    def __init__(self, text: str, text_color: tuple, bg_color: tuple, height: int, width: int): 
        super().__init__()


        self.render_text = pygame.font.render(text, True, text_color)
        self.text_rect = self.render_text.get_rect() 

        
        self.surface = pygame.Surface([width, height]) 
        self.surface.fill(SURFACE_COLOR) 
        self.surface.set_colorkey(COLOR)

        pygame.draw.rect(self.surface,bg_color,pygame.Rect(0, 0, width, height)) 

        self.rect = self.surface.get_rect() 


pygame.init() 

# RED = (255, 0, 0) 

# size = (WIDTH, HEIGHT) 
# screen = pygame.display.set_mode(size) 
# pygame.display.set_caption("Creating Sprite") 

# all_sprites_list = pygame.sprite.Group() 

# # object_ = Sprite(RED, 20, 30) 
# object_.rect.x = 200
# object_.rect.y = 300

# all_sprites_list.add(object_) 

# exit = True
# clock = pygame.time.Clock() 

# while exit: 
# 	for event in pygame.event.get(): 
# 		if event.type == pygame.QUIT: 
# 			exit = False

# 	all_sprites_list.update() 
# 	screen.fill(SURFACE_COLOR) 
# 	all_sprites_list.draw(screen) 
# 	pygame.display.flip() 
# 	clock.tick(60) 

# pygame.quit() 
