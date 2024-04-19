import pygame
class Button(pygame.sprite.Sprite):
    def __init__(
        self, text: str, text_color: tuple, bg_color: tuple
    ):
        super().__init__()

        # default font
        button_font = pygame.font.SysFont("monospace", 20)

        self.render_text = button_font.render(text, True, text_color)
        text_width, text_height = self.render_text.get_size()

        # Adjust dimensions based on text size and padding
        self.width = text_width + 20  # Add padding horizontally
        self.height = text_height + 20  # Add padding vertically

        # Create the button image (background)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect()  # This defines the button's rectangle

        # Calculate text position to center it
        self.text_rect = self.render_text.get_rect(center=self.rect.center)

        # Blit the text onto the button's image
        self.image.blit(self.render_text, self.text_rect)

    def is_clicked(self, event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.text_rect.collidepoint(event.pos)
        )

