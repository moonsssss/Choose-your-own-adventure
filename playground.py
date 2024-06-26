import pygame
import pygame_gui
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 1000, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()

UI_MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((600, 400), (387, 50)),
    manager=UI_MANAGER,
    object_id="main_text_entry"
)


# FONTS
verdana_50 = pygame.font.SysFont("verdana", 14)
verdana_100 = pygame.font.SysFont("verdana", 14)

#MAPS
def shrinkmap(map):
    MAPWIDTH, MAPHEIGHT = map.get_size()
    scaling_factor = HEIGHT/MAPHEIGHT
    finalmap = pygame.transform.smoothscale(map, (int(MAPHEIGHT*scaling_factor), HEIGHT))
    return(finalmap)
Day1Map = pygame.image.load(r"C:\Users\Lochlann\Coding Games\Choose-your-own-adventure\Island.png")
Day1Map = shrinkmap(Day1Map)
Day2Map = pygame.image.load(r"C:\Users\Lochlann\Coding Games\Choose-your-own-adventure\island2.png")
Day2Map = shrinkmap(Day2Map)
Day3Map = pygame.image.load(r"C:\Users\Lochlann\Coding Games\Choose-your-own-adventure\island3.png")
Day3Map = shrinkmap(Day3Map)
Day4Map = pygame.image.load(r"C:\Users\Lochlann\Coding Games\Choose-your-own-adventure\island4.png")
Day4Map = shrinkmap(Day4Map)

class gameState:
    # add any variables for the character here
    user_response = ""  # store/remember the text response of the user
gs = gameState()

def start_of_story(): 
    while True:
        SCREEN.fill((178, 166, 142))
        # 60 frames per second / 1000
        # Controls how fast cursor blinks
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # This allows us to see if we hit enter (finished our text entry)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                # We've pressed enter for text entry

                # Update the user_response variable in the player gamestate
                # Hint: event.text contains whatever they just typed
                gs.user_response = event.text

                if event.text == "1":
                    print("Go hunt")
                    
                    go_hunt()

                    

                elif event.text == "2":
                    print("You keep going")
                    chosen_lottery_ball = random.randint(1, 100)
                    if chosen_lottery_ball < 25:
                        death()
                    else:
                        day_2transition()
                else:
                    print("This isn't an option. ")

                
                    

                # TODO  

            # Pass current event to manager
            UI_MANAGER.process_events(event)

        # Update every UI event in manager
        UI_MANAGER.update(UI_REFRESH_RATE)

        first_prompt = verdana_50.render("This is your first day, you have two options: ", True, "black");
        first_prompt_rect = first_prompt.get_rect(topleft=(600, 5))

        option_1 = verdana_50.render("1. You need to hunt for food, but you will lose a day.", True, "black")
        option_1_rect = first_prompt.get_rect(topleft=(first_prompt_rect.left, first_prompt_rect.bottom + 10))
        
        option_2 = verdana_50.render("2. You can keep going, but you will have a 25% chance \n of dying.", True, "black")
        option_2_rect = first_prompt.get_rect(topleft=(option_1_rect.left, option_1_rect.bottom + 10))

        # Can you add options for the other 3 main directions?
        # TODO

        SCREEN.blit(first_prompt, first_prompt_rect)
        SCREEN.blit(option_1, option_1_rect)
        SCREEN.blit(option_2, option_2_rect)
        SCREEN.blit(Day1Map, (0,0))
       
        


        UI_MANAGER.draw_ui(SCREEN)
        pygame.display.update()


def day_2transition():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((80, 250, 199))
 
        your_text = verdana_50.render(f"Day 2", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)
        
  
        CLOCK.tick(60)
        
        pygame.display.update()

        time.sleep(2)

        day_2()

def day_2():
    TEXT_INPUT.set_text("")
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                # We've pressed enter for text entry

                # Update the user_response variable in the player gamestate
                # Hint: event.text contains whatever they just typed
                gs.user_response = event.text

                if event.text == "1":
                    print("You go around it")
                    
                    day_3transition

                elif event.text == "2":
                    print("You swim through it")
                    chosen_lottery_ball = random.randint(1, 100)
                    if chosen_lottery_ball < 10:
                        death()
                    else:
                        day_3transition()
                else:
                    print("This isn't an option. ")
           
            UI_MANAGER.process_events(event)
        
        UI_MANAGER.update(UI_REFRESH_RATE)
        
        SCREEN.fill((178, 166, 142))
 
        second_prompt = verdana_50.render("This is your second day, you have two options: ", True, "black");
        second_prompt_rect = second_prompt.get_rect(topleft=(600, 5))

        option_1 = verdana_50.render("1.You have to cross a river, you can go around it and \n lose a day .", True, "black")
        option_1_rect = second_prompt.get_rect(topleft=(second_prompt_rect.left, second_prompt_rect.bottom + 10))

        option_2 = verdana_50.render("2. Swim trough it and have a 10% chance of dying!", True, "black")
        option_2_rect = second_prompt.get_rect(topleft=(option_1_rect.left, option_1_rect.bottom + 25))
        
        
        SCREEN.blit(second_prompt, second_prompt_rect)
        SCREEN.blit(option_1, option_1_rect)
        SCREEN.blit(option_2, option_2_rect)
        SCREEN.blit(Day2Map, (0,0))

        

        
        
  
        CLOCK.tick(60)
        
        UI_MANAGER.draw_ui(SCREEN)
        pygame.display.update()
        
        
def day_3transition():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((80, 250, 199))
 
        your_text = verdana_50.render(f"Day 3", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)
        
        
        CLOCK.tick(60)
        
        pygame.display.update()

        time.sleep(2)
        
        
        day_3()

        
        
def day_3():
    
    TEXT_INPUT.set_text("")
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                # We've pressed enter for text entry

                # Update the user_response variable in the player gamestate
                # Hint: event.text contains whatever they just typed
                gs.user_response = event.text

                if event.text == "1":
                    
                    
                    day_4transition

                elif event.text == "2":
        
                    chosen_lottery_ball = random.randint(1, 100)
                    if chosen_lottery_ball < 35:
                        death()
                    else:
                        day_4transition()
                else:
                    print("This isn't an option. ")
           
            UI_MANAGER.process_events(event)
        
        UI_MANAGER.update(UI_REFRESH_RATE)
        
        SCREEN.fill((178, 166, 142))
 
        third_prompt = verdana_50.render("This is your third day, you have two options: ", True, "black");
        third_prompt_rect = third_prompt.get_rect(topleft=(600, 5))

        option_1 = verdana_50.render("1. You can go through a cave where you can get water \n but you will lose a day", True, "black")
        option_1_rect = third_prompt.get_rect(topleft=(third_prompt_rect.left, third_prompt_rect.bottom + 10))

        option_2 = verdana_50.render("2. Reject the offer, but you have a 35% chance of dying", True, "black")
        option_2_rect = third_prompt.get_rect(topleft=(option_1_rect.left, option_1_rect.bottom + 25))

        
        SCREEN.blit(third_prompt, third_prompt_rect)
        SCREEN.blit(option_1, option_1_rect)
        SCREEN.blit(option_2, option_2_rect)
        SCREEN.blit(Day3Map, (0,0))

        pygame.display.update()


def day_4transition():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((80, 250, 199))
 
        your_text = verdana_50.render(f"Day 4", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)
        
        
        CLOCK.tick(60)
        
        pygame.display.update()

        time.sleep(2)

        day_4()

def day_4():
    TEXT_INPUT.set_text("")
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                # We've pressed enter for text entry

                # Update the user_response variable in the player gamestate
                # Hint: event.text contains whatever they just typed
                gs.user_response = event.text

                if event.text == "2":
                    
                    
                    day_4transition

                elif event.text == "1":
        
                    chosen_lottery_ball = random.randint(1, 100)
                    if chosen_lottery_ball < 35:
                        death()
                    else:
                        day_4transition()
                else:
                    print("This isn't an option. ")
           
            UI_MANAGER.process_events(event)
        
        UI_MANAGER.update(UI_REFRESH_RATE)
        
        SCREEN.fill((178, 166, 142))
 
        forth_prompt = verdana_50.render("This is your third day, you have two options: ", True, "black");
        forth_prompt_rect = forth_prompt.get_rect(topleft=(600, 5))

        option_1 = verdana_50.render("1. You can kill a bear and if you do you get food for 4 days \n but there is a 65% chance you die", True, "black")
        option_1_rect = forth_prompt.get_rect(topleft=(forth_prompt_rect.left, forth_prompt_rect.bottom + 10))

        option_2 = verdana_50.render("2. You can reject the offer and keep going", True, "black")
        option_2_rect = forth_prompt.get_rect(topleft=(option_1_rect.left, option_1_rect.bottom + 25))

        
        SCREEN.blit(forth_prompt, forth_prompt_rect)
        SCREEN.blit(option_1, option_1_rect)
        SCREEN.blit(option_2, option_2_rect)
        SCREEN.blit(Day4Map, (0,0))       
        
  
        CLOCK.tick(60)
        
        UI_MANAGER.draw_ui(SCREEN)
        pygame.display.update()
  
        CLOCK.tick(60)
        
        pygame.display.update()



       


           
  

def death():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((255, 0, 0))
 
        your_text = verdana_50.render(f"You Died!", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)


        CLOCK.tick(60)

        pygame.display.update()





def go_hunt():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((80, 250, 199))

        your_text = verdana_50.render(f"Hunting...", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)

        pygame.display.update() 
        
        time.sleep(2)

        day_2transition()

        CLOCK.tick(60)

        pygame.display.update()
    



start_of_story()
