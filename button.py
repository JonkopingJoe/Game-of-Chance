import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, text: str, text_color: tuple, bg_color: tuple, font, size):
        super().__init__()

        button_font = pygame.font.SysFont(font, size)

        self.render_text = button_font.render(text, True, text_color)
        text_width, text_height = self.render_text.get_size()

        # Adjust dimensions based on text size and padding
        self.width = text_width + 20  # Add padding horizontally
        self.height = text_height + 20  # Add padding vertically

        # Create the button image (background)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect()  # This defines the button's rectangle

        # Calculate text position to center it on the rectangle
        self.text_rect = self.render_text.get_rect(center=self.rect.center)

        # Blit the text onto the button's image
        self.image.blit(self.render_text, self.text_rect)

        # mouse is not clicked
        self.clicked = False

    def is_clicked(self):  # method for an instance of the button class to detect a click
        action = False
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse cursor is over the button's rectangle (self.rect)
        if self.rect.collidepoint(mouse_pos):

            # check if the left mouse has been clicked that ensure that prolonged clicking will have no effect
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action
