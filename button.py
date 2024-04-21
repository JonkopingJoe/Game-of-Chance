import pygame

"""
    This is a clickable button class for Pygame.

    Parameters:
    text (str): The text to display on the button.
    text_color (tuple): The color of the text.
    bg_color (tuple): The background color of the button.
    font (str, optional): The font to use. Defaults to "monospace".
    size (int, optional): The font size. Defaults to 15.

    Attributes:
    width (int): The width of the button.
    height (int): The height of the button.
    image (pygame.Surface): The button's image.
    rect (pygame.Rect): The button's rectangle.
    text_rect (pygame.Rect): The text's rectangle.
    clicked (bool): Whether the button is currently clicked.

    Methods:
    is_clicked() -> bool: Returns True if the button is clicked, False otherwise.
"""


class Button(pygame.sprite.Sprite):
    def __init__(
        self, text: str, text_color: tuple, bg_color: tuple, font="monospace", size=15
    ):
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

    def is_clicked(
        self,
    ):  # method for an instance of the button class to detect a click
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(
            mouse_pos
        ):  # Check if the mouse cursor is over the button's rectangle (self.rect)

            # check if the left mouse has been clicked that ensure that prolonged clicking will have no effect
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action
