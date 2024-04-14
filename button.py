import pygame

pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, text: str, text_color: tuple, bg_color: tuple, height: int, width: int):
        super().__init__()

        # Default font
        font = pygame.font.Font(None, 36)

        # Render text
        self.render_text = font.render(text, True, text_color)
        self.text_rect = self.render_text.get_rect()

        # Display surface
        self.surface = pygame.Surface([width, height])
        self.surface.fill(bg_color)

        # Align text centre with surface centre
        self.text_rect.center = self.surface.get_rect().center

        # Display surface
        self.surface.blit(self.render_text, self.text_rect)

        # Store rect
        self.rect = self.surface.get_rect()

screen = pygame.display.set_mode((800, 600))
button = Button("Click Me!", (255, 255, 255), (0, 128, 255), 50, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                print("Button Clicked!")

    screen.fill((0, 0, 0))
    screen.blit(button.surface, (300, 275))
    pygame.display.flip()

pygame.quit()
