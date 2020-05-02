## This module has the size method which returns the length and weight of the computer's screen
import pyautogui
import pygame

class Settings:
    def __init__(self,screen):
        # Set inital bankroll
        

        # Set the ingame text font, size and color
        self.font = pygame.font.Font(None, 52)
        self.text_color = (0,0,0)

        # Pair the settings with the main screen
        self.screen_rect = screen.screen.get_rect()
        
        
        # Get the screen's resolution
        self.screen_length = pyautogui.size()[0]
        self.screen_height = pyautogui.size()[1]
        
        # Set colors for the background screens
        self.background_color = (34, 180, 115)

        
        # Size of player and comp texts
        
        self.space_x=self.screen_length//25
        self.space_y=self.screen_height//25
        
        self.player_screen_length=self.screen_length//3
        self.player_screen_heigth=self.screen_height*3//5


        self.computer_screen_length=self.screen_length//3
        self.computer_screen_heigth=self.screen_height//5



   