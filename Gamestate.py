import pygame, sys, os

pygame.init()


class GameState:
    def __init__(self):
        # self.button = button
        # self.state_image = state_image
        # self.state_sound = state_sound
        pygame.init()
        SCREEN = pygame.display.set_mode((1280, 720))
        pygame.mixer.init() 
        pygame.font.init() 


    def load_images(self, image_name): 
        """Method to load all images correctly from the system folder into a dictionary

        Arg: No positional argument

        Returns: A dictionary where the keys are image filenames/scenarios and values are pygame surface objects

        Usage: 
        test = GameState()
        test.load_images()
        """
        images = {}
        
        images_folder = r"C:\Users\rgnpx\Stuff\CS\Game-of-Chance\images"
        if not os.path.isdir(images_folder):
            print(f"Error: {images_folder} provided is not a valid directory")
        
        for image_name in os.listdir(images_folder): 
            image = os.path.join(images_folder, image_name)
            if os.path.isfile(image):
                try:
                    image_name.lower().endswith(('.png', '.jpg.', '.webp'))
                    image = pygame.image.load(image).convert_alpha()
                    images[image_name] = image
                except pygame.error as e:
                    print(f"Error loading image {image_name}: {e}")
                    raise SystemExit
        return image
    def load_image(self, name, colorkey=None, scale=1):
        fullname = os.path.join(r"", name)
        image = pygame.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pygame.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey ==- -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()
    

    
    def load_sounds(self, sound) -> dict:

        sounds = {}

        sounds_folder = r"C:\Users\reaga\Documents\Class Stuff\CS\Game-of-Chance\audio"
        if not os.path.isdir(sounds_folder):
            print(f"Error: {sounds_folder} provided is not a valid directory")
        
        for a_sound in os.listdir(sounds_folder):
            sound_path = os.path.join(sounds_folder, a_sound)
            if os.path.isfile(sound_path):
                try:
                    a_sound.endswith(('.aac', '.mp3', '.wav'))
                    sound = pygame.mixer.Sound(sound_path)
                    sounds[a_sound] = sound
                except pygame.error as e:
                    print(f" Error Playing the sound {a_sound}: {e}")
                    raise SystemExit
        return sound

    def mouse_click(self, button): # checks if the mouse is clicked on the rect
        # we can only click the following buttons, so set up arguments to be those buttons upon call of this method
        pass


    def key_press(self, key):
        # for event in pygame.event.get():
        #     if event.type == pygame.K_1:
        #         # pressed 1, goes to front door
        pass
            

    def show_image_surface(self, image, position:tuple):
        # Display an image on the screen
        # WINDOW.blit(image, position)
        pass

    def show_text(self, text, position:tuple, font_size:int, font_color:tuple, font_type:str):
        # Render and display text on the screen
        font = pygame.font.SysFont(font_type, font_size)
        text_surface = font.render(text, True, font_color)
        # WINDOW.blit(text_surface, position)



class MainMenu(GameState):
    def __init__(self):
        super().__init__('main_menu')

    def run(self):
        # load the background
        # load the music
        # load the text
        # load the buttons

    
        pass

def run():
    pygame.init()

    # creating the backgound
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("TESTINGGG, HELLOO?")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))
    
    # put some text into the background, centered
    if pygame.font:
        font = pygame.font.Font(None, 64) # create a font object
        text = font.render("You Know What It Is, Testing Baby!", True, (10, 10, 10)) # render it
        textpos = text.get_rect(centerx=background.get_width()/2, y = 10) # find the center of the background
        background.blit(text, textpos) # paste the text

    # main loop ... events still
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # normal exit method
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # exit using ESC key
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pass
            
        # show the screen now
        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == '__main__':
    run()

            
# prepare objects
some_sound = GameState().load_sounds("intro")
some_image = GameState().load_images("pond")

"""
set up objects
Draw them:
    screen.blit(background, (0,0))
    objects.draw()
"""