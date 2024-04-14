import pygame
from random import randint, choice
from scenario import Scenario
from structlinks import LinkedList

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LUCKOMETER")
        self.state = 'menu'
        self.screen = pygame.display.set_mode((720, 520))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 12)
        self.luck_score = 100
        self.scenarios_list = self.initialize_game_scenarios_list()
    


    # Displaying Seciton

    def get_text_rect(self, text, x, y) -> tuple:
        rendered_text = self.font.render(text, True, (255, 255, 255))
        text_rect = rendered_text.get_rect(center=(x, y))
        return rendered_text, text_rect

    def display_surface(self, surface: pygame.Surface, x: int, y: int) -> None: 
        self.screen.blit(surface, (x, y))
        return None
    

    def display_image(self, image_path: str, x: int, y: int) -> None:
        self.screen.blit(image_path, (x, y))
        return None 

    
    def initialize_game_scenarios_list(self) -> list: 
        scenarios_list = []


        # scenario one
        train_watting = Scenario("./waittrain_late_small.jpg") 
        train_watting.set_cases(

            # First
            "wait for the train", 
            "you catched the train", 
            "the train was tirmminated", 

            ## Second 
            "skip the train and book an uber", 
            "you skipped the train and the uber is too expensive", 
            "the uber is cheaper", 
        ) 


        # appending scenario

        return scenarios_list 

    def get_scenarios_flow(self) -> LinkedList: 
        scenario_flow_linkedList = LinkedList() 

        while len(scenario_flow_linkedList) < 4: # The full game loop is made of four scenarios. 
            random_scenario = choice(self.scenarios_list())

            if random_scenario not in scenario_flow_linkedList: 
                scenario_flow_linkedList.append(random_scenario)
        
        return scenario_flow_linkedList

    


    
    # Todo: fix this funciton
    def make_button(x: int, y: int, width: int, height: int) -> pygame.Rect: 

        # Create a surface for the button
        button_surface = pygame.Surface((width, height))

        # Create a pygame.Rect object that represents the button's boundaries
        button_rect = pygame.Rect(x, y, width, height)  # Adjust the position as needed

        return button_surface,

    
    def main_menu(self) -> None: 
        self.display_image("pictures/game_background.png")


    # Luck Changing function 
    def random_luck_diff(self) -> int:
        # return the change in luck
        return randint(-10, 10)



    def run(self):
    # !!!Could make it a independent class
    # We may create an independent classes of game_state, and call them here
        while True:
            self.screen.fill((0, 0, 0))
            self.handle_events()

            # Integrate following block into class menu = GameState('menu')
            if self.state == 'menu':
                self.display_background(self.city) # May be integrated with show_menu
                self.show_menu()
            # Integrate following block into class game = GameState('game')
            elif self.state == 'game':
                self.display_background(self.pond_background) # May be integrated with a new Event class
                self.display_luck()
                self.create_game_options()
            # Integrate following block into class event = GameState('event')
            elif self.state == 'event_end':
                # self.screen.fill((0, 0, 0))
                change_text = f"Your lucky point changed {self.last_change:+d}."
                self.display_text(change_text, self.screen.get_width()/2, self.screen.get_height()/2 - 50)
                prompt_text = "Press SPACE to continue."
                self.display_text(prompt_text, self.screen.get_width()/2, self.screen.get_height()/2 + 50)
            # Integrate following block into class end = GameState('end')
            elif self.state == 'end':
                # self.screen.fill((0, 0, 0))
                final_text = f"Let's call this a day, your final lucky point is {self.luck}."
                self.display_text(final_text, self.screen.get_width()/2, self.screen.get_height()/2 - 50)
                prompt_text = "Press SPACE to return to the main menu."
                self.display_text(prompt_text, self.screen.get_width()/2, self.screen.get_height()/2 + 50)
            
            pygame.display.flip()
            self.clock.tick(60)

            


    

    