from lib.Settings import Settings
import pygame

class Pictures:
    def __init__(self,screen):
        ''' 
        With this class I am going to load the pictures and texts that will 
        show up in the different stages of the game
        '''
        # Initialize the game screen and load dependent classes
        self.screen = screen.screen
        self.settings = Settings(self)

        # Get coordinates of screen size and center points
        self.screen_rect = self.screen.get_rect()
        self.screen_rect_center = self.screen_rect.center

        self.screen_x = self.screen_rect[2]
        self.screen_y = self.screen_rect[3]

        self.screen_center_x = self.screen_rect_center[0]
        self.screen_center_y = self.screen_rect_center[1]


        # Initalize flags and other variables
        self.intro = True
        self.player_has_hit = self.play_stage = self.end_stage = False
        self.bet_stage = self.over_21 = self.player_hit = self.update = False
        self.bankroll = 1000
        self.current_bet = 0

        '''Load up the pictures'''
        # Load INTRO menu pictures
        self.intro_text_1 = pygame.image.load("assets/intro_text_1.png")
        self.intro_text_2 = pygame.image.load("assets/intro_text_2.png")
        self.intro_cards = pygame.image.load("assets/intro_cards.png")
        self.intro_quit = pygame.image.load("assets/Quit.png")
        self.intro_play = pygame.image.load("assets/Play.png")


        # Load BET STAGE menu pictures
        self.bet_100 = pygame.image.load("assets/100.png")
        self.bet_200 = pygame.image.load("assets/200.png")
        self.bet_500 = pygame.image.load("assets/500.png")
        self.bet_done = pygame.image.load("assets/submit.png")
        self.bet_reset = pygame.image.load("assets/reset.png")


        # Load ACTUAL GAME STAGE menu pictures
        self.play_hit = pygame.image.load("assets/Hit.png")
        self.play_double = pygame.image.load("assets/Double.png")            
        self.play_stand = pygame.image.load("assets/Stand.png")


        ''' Initialise onscreen text objects'''
        # Load BET STAGE text objects
        self.bet_text = self.settings.font.render(
            "Please make your bets!",
            True,
            self.settings.textColor
        )
        
        ''' Set up the coordinates of each picture/text object'''
        # set up INTRO stage elements' coordinates
        self.intro_play_x = int(
            self.screen_x/5  - self.intro_play.get_rect ()[2] / 2
            )
        self.intro_play_y = int(
            self.screen_center_y - self.intro_play.get_rect ()[3] /2
            )

        self.intro_quit_x = int(self.screen_x*4/5 - self.intro_quit.get_rect ()[2] /2)
        self.intro_quit_y = int(self.screen_center_y - self.intro_quit.get_rect ()[3]/2)

        self.intro_cards_x = int(self.screen_center_x - self.intro_cards.get_rect ()[2]/2)
        self.intro_cards_y = int(self.screen_center_y - self.intro_cards.get_rect ()[3]/2)

        self.intro_text_1_x = int(self.screen_center_x - self.intro_text_1.get_rect ()[2]/2)
        self.intro_text_1_y = int(self.screen_center_y/3 - self.intro_text_1.get_rect ()[3]/2)

        self.intro_text_2_x = int(self.screen_center_x - self.intro_text_2.get_rect ()[2]/2)
        self.intro_text_2_y = int(self.screen_y - self.screen_center_y*1/3 - self.intro_text_2.get_rect ()[3]/2)


        # Set up BET STAGE elements' coordinates
        self.bet_done_x = int(self.screen_x //8 - self.bet_done.get_rect()[2] // 2)
        self.bet_done_y = int(self.screen_y * 3//5)
        
        self.bet_100_x = int(self.screen_x * 2//8 - self.bet_100.get_rect()[2] // 2)
        self.bet_100_y = int(self.screen_y * 3//5 + self.bet_100.get_rect()[3] // 4)
        
        self.bet_200_x = int(self.screen_x * 4//8 - self.bet_200.get_rect()[2] // 2)
        self.bet_200_y = int(self.screen_y * 3//5 - self.bet_200.get_rect()[3] // 4)
        
        self.bet_500_x = int(self.screen_x * 6//8 - self.bet_500.get_rect()[2] // 2)
        self.bet_500_y = int(self.screen_y * 3//5 + self.bet_500.get_rect()[3] // 4)
 
        self.bet_reset_x = int(self.screen_x * 7//8 - self.bet_reset.get_rect()[2] // 2)
        self.bet_reset_y = int(self.screen_y * 3//5)

        
        ''' Card Game elements'''
        # Set up ACTUAL GAME stage elements' coordinates
        self.play_hit_x = int(self.screen_center_x // 2 - self.play_hit.get_rect()[2] // 2)
        self.play_hit_y = int(self.screen_center_y * 1.5)

        self.play_double_x = int(self.screen_center_x - self.play_double.get_rect()[2] // 2)
        self.play_double_y = int(self.screen_center_y * 1.6) 

        self.play_stand_x = int(self.screen_center_x * 1.5 - self.play_stand.get_rect()[2] // 2) 
        self.play_stand_y = int(self.screen_center_y * 1.5)


    def blitme(self, screen):
        '''Depending on the stage the game is running, we choose what elements to show on the screen'''
        self.screen.fill(self.settings.backgroundColor)

        # Show elements for the INTRO menu
        if self.intro:
        
            self.screen.blit(
                self.intro_text_1,
                (self.intro_text_1_x, self.intro_text_1_y)
            )
            
            self.screen.blit(
                self.intro_text_2,
                (self.intro_text_2_x, self.intro_text_2_y)
            )
            
            self.screen.blit(
                self.intro_play,
                (self.intro_play_x, self.intro_play_y)
            )
            
            self.screen.blit(
                self.intro_quit,
                (self.intro_quit_x, self.intro_quit_y)
            )

            self.screen.blit(
                self.intro_cards,
                (self.intro_cards_x, self.intro_cards_y)
            )

        if self.bet_stage:
            # Load up text
            self.bet_bankroll = self.settings.font.render(
                f"Your current bankroll is: {self.bankroll}",
                True,
                self.settings.textColor
            )

            self.bet_bet = self.settings.font.render(
                f"Your current bet is: {self.current_bet}",
                True,
                self.settings.textColor
            )

            self.screen.blit(
                self.bet_text,
                (self.screen_rect.center[0]-self.bet_text.get_rect()[2] / 2,
                self.screen.get_rect()[3] / 5)
            )
            
            self.screen.blit(
                self.bet_bankroll,
                (self.screen_rect.center[0]-self.bet_bankroll.get_rect()[2] / 2,
                self.screen.get_rect()[3] * 2 / 5)
            )
            
            self.screen.blit(
                self.bet_bet,
                (self.screen_rect.center[0]-self.bet_bet.get_rect()[2] / 2,
                self.screen.get_rect()[3] * 2 / 5 + self.settings.space_y)
            )
            
            self.screen.blit(
                self.bet_done,
                (self.bet_done_x, self.bet_done_y)
            )
            
            self.screen.blit(
                self.bet_100,
                (self.bet_100_x, self.bet_100_y)
            )
            
            self.screen.blit(
                self.bet_200,
                (self.bet_200_x, self.bet_200_y)
            )
            
            self.screen.blit(
                self.bet_500,
                (self.bet_500_x, self.bet_500_y)
            )
            
            self.screen.blit(
                self.bet_reset,
                (self.bet_reset_x, self.bet_reset_y)
            )
            
    
        if self.play_stage:
            if screen.playerscreen.cardPoints == 21:
                screen.computerscreen.stage = "Dealer"
            
            screen.playerscreen.blitme()
            screen.computerscreen.blitme()
            
            self.screen.blit(
                self.play_hit,
                (self.play_hit_x, self.play_hit_y)
            )
        
            if not self.player_hit:
                self.screen.blit(
                    self.play_double,
                    (self.play_double_y, self.play_double_y)
                )
            
            self.screen.blit(
                self.play_stand, 
                (self.play_stand_x, self.play_stand_y)
            )
            
            if screen.computerscreen.stage == "Dealer":
                if screen.computerscreen.cardPoints < 17:
                    screen.computerscreen.hit_card()

                if screen.computerscreen.cardPoints > 16:
                    self.play_stage = False
                    self.end_stage = True
                    
                    
        if self.end_stage == True:
            # Load up text elements
            self.lost_text = self.settings.font.render(
                "Sorry, you lost this hand! Press R to play a new hand or Q to exit!",
                True,
                self.settings.textColor
            )

            self.win_text = self.settings.font.render(
                f"Congratulations, you won {self.current_bet} coins! Press R to play a new hand or Q to exit!",
                True,
                self.settings.textColor
            )
                
            # Set up END GAME stage element's coordinates
            self.lost_text_x = self.screen_center_x - self.lost_text.get_rect()[2]//2
            self.lost_text_y = self.screen_center_y - self.lost_text.get_rect()[3]

            self.win_text_x = self.screen_center_x -  self.win_text.get_rect()[2]//2
            self.win_text_y = self.screen_center_y - self.win_text.get_rect()[3]


            screen.playerscreen.blitme()
            screen.computerscreen.blitme()

            
            if (
                self.over_21 or (
                screen.playerscreen.cardPoints <= screen.computerscreen.cardPoints and 
                screen.computerscreen.cardPoints < 22
                )
            ):
                self.screen.blit(self.lost_text, (self.lost_text_x, self.lost_text_y))
                
                if not self.update:
                    self.bankroll -= self.current_bet
                    self.update = True



            if ((
                screen.playerscreen.cardPoints > screen.computerscreen.cardPoints and 
            not self.over_21
            ) or (
                screen.playerscreen.cardPoints < 22 and
                screen.computerscreen.cardPoints > 21
                )
            ):
                self.screen.blit(self.win_text, (self.win_text_x, self.win_text_y))
                if not self.update:
                    self.bankroll += self.current_bet
                    self.update = True