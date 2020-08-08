import sys
import pygame

from lib.Settings import Settings
from lib.Cards import Cards
from lib.Pictures import Pictures


class BlackJack:
    def __init__(self):
        # Initialize the game and settings from Settings class
        pygame.init()
        

        # Initialize the game screen in fullscreen mode
        self.screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)        
        

        # Creates instances of te other classes     
        self.settings = Settings(self)
        self.playerscreen = Cards (self, "Player")
        self.computerscreen = Cards (self, "Dealer")   
        self.pictures = Pictures(self)
    
    def playGame(self):
        '''Start the main loop of the game'''
        while True:
            self._updateScreen()
            self._checkEvents()
            self._checkGameStatus()


    def _checkGameStatus(self):
        if self.playerscreen.cardPoints > 21:
            self.pictures.play_stage = False
            self.pictures.end_stage = self.pictures.over_21 = True


            
    def _checkEvents(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
                
            elif event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_r: self._redeal_hand()
                                                     
                elif event.key == pygame.K_q: sys.exit()

            # Buttons in INTRO menu        
            if (
                event.type == pygame.MOUSEBUTTONDOWN and 
                event.button == 1 and 
                self.pictures.intro
            ):

                mouse=pygame.mouse.get_pos()
                # Press PLAY button
                if (mouse[0] in range(
                    self.pictures.intro_play_x,
                    self.pictures.intro_play_x + self.pictures.intro_play.get_rect()[2]
                    ) and 
                    mouse[1] in range(
                        self.pictures.intro_play_y,
                        self.pictures.intro_play_y + self.pictures.intro_play.get_rect()[3]
                    )
                ):                    
                    self.pictures.bet_stage = True
                    self.pictures.intro = False

                # Press QUIT button
                if (mouse[0] in range(
                    self.pictures.intro_quit_x,
                    self.pictures.intro_quit_x + self.pictures.intro_quit.get_rect()[2]
                    ) and 
                    mouse[1]in range(
                        self.pictures.intro_quit_y,
                        self.pictures.intro_quit_y + self.pictures.intro_quit.get_rect()[3]
                    )
                ):
                    sys.exit()                    
                
            # Buttons in BET STAGE menu
            if (
                event.type == pygame.MOUSEBUTTONDOWN and 
                event.button == 1 and 
                self.pictures.bet_stage == True
                ): 
                
                mouse = pygame.mouse.get_pos()
                
                if (
                    mouse[0] in range(
                    self.pictures.bet_done_x,
                    self.pictures.bet_done_x + self.pictures.bet_done.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.bet_done_y,
                        self.pictures.bet_done_y + self.pictures.bet_done.get_rect()[3]
                    )
                ):
                    self.pictures.play_stage = True
                    self.pictures.bet_stage = False
                    
                if (
                    mouse[0] in range(
                    self.pictures.bet_100_x
                    ,self.pictures.bet_100_x + self.pictures.bet_100.get_rect()[2]
                    ) and  
                    mouse[1] in range(self.pictures.bet_100_y,
                    self.pictures.bet_100_y + self.pictures.bet_100.get_rect()[3]
                    )
                ):
                    self.pictures.current_bet += 100

                    if self.pictures.current_bet > self.pictures.bankroll:
                        self.pictures.current_bet = self.pictures.bankroll
                
                if (
                    mouse[0] in range(
                    self.pictures.bet_200_x,
                    self.pictures.bet_200_x + self.pictures.bet_done.get_rect()[2]
                    ) and  
                    mouse[1] in range(self.pictures.bet_200_y,
                    self.pictures.bet_200_y + self.pictures.bet_200.get_rect()[3]
                    )
                ):
                    self.pictures.current_bet += 200
                    if self.pictures.current_bet > self.pictures.bankroll:
                        self.pictures.current_bet = self.pictures.bankroll

                if (
                    mouse[0] in range(
                    self.pictures.bet_500_x,
                    self.pictures.bet_500_x + self.pictures.bet_500.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.bet_500_y,
                        self.pictures.bet_500_y + self.pictures.bet_500.get_rect()[3]
                    )
                ):
                    self.pictures.current_bet += 500
                    if self.pictures.current_bet > self.pictures.bankroll:
                        self.pictures.current_bet = self.pictures.bankroll

                if (
                    mouse[0] in range(
                    self.pictures.bet_reset_x,
                    self.pictures.bet_reset_x + self.pictures.bet_reset.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.bet_reset_y,
                        self.pictures.bet_reset_y + self.pictures.bet_reset.get_rect()[3]
                    )
                ):
                    self.pictures.current_bet = 0

            if (
                event.type == pygame.MOUSEBUTTONDOWN and 
                event.button == 1 and 
                self.pictures.play_stage
            ):
                mouse=pygame.mouse.get_pos()
           
                if (
                    mouse[0] in range(
                    self.pictures.play_hit_x,
                    self.pictures.play_hit_x + self.pictures.play_hit.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.play_hit_y,
                        self.pictures.play_hit_y + self.pictures.play_hit.get_rect()[3]
                    )
                ):
                    self.pictures.player_has_hit = True
                    self.playerscreen.hit_card()
                    self.pictures.player_hit = True

                if (
                    mouse[0] in range(
                    self.pictures.play_double_x,
                    self.pictures.play_double_x + self.pictures.play_double.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.play_double_y, self.pictures.play_double_y+self.pictures.play_double.get_rect()[3]
                    ) and 
                    self.pictures.player_hit == False
                ):
                    self.playerscreen.hit_card()
                    self.computerscreen.stage = "Dealer"
                    self.pictures.current_bet *= 2

                if (
                    mouse[0] in range(
                        self.pictures.play_stand_x,
                        self.pictures.play_stand_x + self.pictures.play_stand.get_rect()[2]
                    ) and  
                    mouse[1] in range(
                        self.pictures.play_stand_y,
                        self.pictures.play_stand_y + self.pictures.play_stand.get_rect()[3]
                    )
                ):
                     self.computerscreen.stage = "Dealer"

    def _updateScreen(self):
        '''Update images on the screen, and flip to new screen'''
        # Redraw the screen during each pass through the loop
        self.pictures.blitme(self)
        # Make the most recently drawn screen visible
        pygame.display.flip()


    def _redeal_hand(self):
        self.pictures.bet_stage = True
        self.pictures.end_stage = self.pictures.over_21 = False
        self.computerscreen.remake_cards()
        self.playerscreen.remake_cards()
        self.computerscreen.stage = "Player"
        self.pictures.current_bet = 0
        self.pictures.player_hit = self.pictures.update = False
        if self.pictures.bankroll <= 0:
            self.pictures.bankroll = 1000


if __name__=='__main__':
    bj=BlackJack()
    bj.playGame()