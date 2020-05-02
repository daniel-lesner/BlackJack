import sys
import pygame

from settings import Settings
from Cards import Cards


class BlackJack:
    def __init__(self):
        ''' Initialize the game and settings from Settings class'''
        pygame.init()
        
        ''' Set up the game screen'''
        self.screen = pygame.display.set_mode ( (0, 0), pygame.FULLSCREEN )        
        
        ''' Creates instances of te other classes'''        
        self.settings = Settings ( self )
        self.playerscreen = Cards ( self, "Player" )
        self.computerscreen = Cards ( self, "Dealer" )   

    
    def run_game(self):
        '''Start the main loop of the game'''
        while True:
            self._update_screen()
            self._check_events()
            self._check_status_of_game()


    def _check_status_of_game(self):
        if self.playerscreen.points_cards > 21:
            self.settings.end_stage = self.settings.over_21 = True
            self.settings.play_stage = False

            
    def _check_events(self):
        ''' Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_r:
                    # Start a new round
                    self._redeal_hand()
                                                     
                elif event.key==pygame.K_q:
                    sys.exit()
                    
            if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1 and self.settings.intro==True:
                mouse=pygame.mouse.get_pos()
                if mouse[0]in range ( self.settings.screen_rect[2]//5  - self.intro_play.get_rect ()[2]//2,
                                      self.settings.screen_rect[2]//5  - self.intro_play.get_rect ()[2]//2 + self.intro_play.get_rect()[2] ) and mouse[1]in range ( self.settings.screen_rect.center[1] - self.intro_play.get_rect ()[3]//2,self.settings.screen_rect.center[1] - self.intro_play.get_rect ()[3]//2 + self.intro_play.get_rect()[3]):
                    self.settings.bet_stage=True
                    self.settings.intro=False
                if mouse[0]in range ( self.settings.screen_rect[2]*4//5 - self.intro_quit.get_rect ()[2]//2,
                                      self.settings.screen_rect[2]*4//5 - self.intro_quit.get_rect ()[2]//2 + self.intro_quit.get_rect()[2] ) and mouse[1]in range(
                                          self.settings.screen_rect.center[1] - self.intro_quit.get_rect ()[3]//2,
                                          self.settings.screen_rect.center[1] - self.intro_quit.get_rect ()[3]//2 + self.intro_quit.get_rect()[3]):
                    sys.exit()                    
                
                
            if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1 and self.settings.bet_stage==True:
                mouse=pygame.mouse.get_pos()
                
                if mouse[0]in range (  self.bet_done_x
                                       ,self.bet_done_x+self.bet_done.get_rect()[2]) and  mouse[1]in range ( self.bet_done_y,
                                                                                                             self.bet_done_y+self.bet_done.get_rect()[3]):
                    self.settings.play_stage=True
                    self.settings.bet_stage=False
                    
                if mouse[0]in range (  self.bet_100_x
                                       ,self.bet_100_x+self.bet_100.get_rect()[2]) and  mouse[1]in range ( self.bet_100_y,
                                                                                                             self.bet_100_y+self.bet_100.get_rect()[3]):
                    self.settings.current_bet+=100
                    if self.settings.current_bet>self.settings.bankroll:
                        self.settings.current_bet=self.settings.bankroll
                
                if mouse[0]in range (  self.bet_200_x
                                       ,self.bet_200_x+self.bet_done.get_rect()[2]) and  mouse[1]in range ( self.bet_200_y,
                                                                                                             self.bet_200_y+self.bet_200.get_rect()[3]):
                    self.settings.current_bet+=200
                    if self.settings.current_bet>self.settings.bankroll:
                        self.settings.current_bet=self.settings.bankroll

                if mouse[0]in range (  self.bet_500_x
                                       ,self.bet_500_x+self.bet_500.get_rect()[2]) and  mouse[1]in range ( self.bet_500_y,
                                                                                                             self.bet_500_y+self.bet_500.get_rect()[3]):
                    self.settings.current_bet+=500
                    if self.settings.current_bet>self.settings.bankroll:
                        self.settings.current_bet=self.settings.bankroll

                if mouse[0]in range (  self.bet_reset_x
                                       ,self.bet_reset_x+self.bet_reset.get_rect()[2]) and  mouse[1]in range ( self.bet_reset_y,
                                                                                                             self.bet_reset_y+self.bet_reset.get_rect()[3]):
                    self.settings.current_bet=0

            if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1 and self.settings.play_stage == True:
                mouse=pygame.mouse.get_pos()
           
                if (mouse[0]in range (  self.play_hit_x,self.play_hit_x + self.play_hit.get_rect()[2]) 
                and  mouse[1]in range ( self.play_hit_y, self.play_hit_y+self.play_hit.get_rect()[3])):
                    self.settings.player_has_hit=True
                    self.playerscreen.hit_card()
                    self.settings.player_hit=True

                if (mouse[0]in range (  self.play_double_x ,self.play_double_x+self.play_double.get_rect()[2]) 
                                       and  mouse[1]in range ( self.play_double_y, self.play_double_y+self.play_double.get_rect()[3]) 
                                       and self.settings.player_hit==False):
                    self.playerscreen.hit_card()
                    self.computerscreen.stage="Dealer"
                    self.settings.current_bet*=2

                if (mouse[0]in range (  self.play_stand_x, self.play_stand_x + self.play_stand.get_rect()[2]) 
                and  mouse[1]in range ( self.play_stand_y, self.play_stand_y + self.play_stand.get_rect()[3])):
                     self.computerscreen.stage="Dealer"

    def _update_screen(self):
        '''Update images on the screen, and flip to new screen'''
        # Redraw the screen during each pass through the loop
        ''' Intro Screen elements'''

        self.intro_text_1=pygame.image.load("Pictures/intro_text_1.png")
        self.intro_text_2=pygame.image.load("Pictures/intro_text_2.png")
        self.intro_cards=pygame.image.load("Pictures/intro_cards.png")
        self.intro_quit=pygame.image.load("Pictures/Quit.png")
        self.intro_play=pygame.image.load("Pictures/Play.png")
        self.intro_rect=self.screen.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.intro_rect.center=self.screen_rect.center
        
        ''' Bet Screen elements'''
        self.bet_bankroll=self.settings.font.render(f"Your current bankroll is: {self.settings.bankroll}",True, (0,0,0))
        self.bet_bet=self.settings.font.render(f"Your current bet is: {self.settings.current_bet}", True, (0,0,0))
        self.bet_text=self.settings.font.render("Please make your bets!", True, (0,0,0))
        
        self.bet_100=pygame.image.load("Pictures/100.png")
        self.bet_200=pygame.image.load("Pictures/200.png")
        self.bet_500=pygame.image.load("Pictures/500.png")
        self.bet_done=pygame.image.load("Pictures/submit.png")
        self.bet_reset=pygame.image.load("Pictures/reset.png")
        
        self.bet_done_x=self.screen.get_rect()[2]//8 - self.bet_done.get_rect()[2]//2
        self.bet_done_y=self.screen.get_rect()[3]*3//5
        
        self.bet_100_x=self.screen.get_rect()[2]*2//8 - self.bet_100.get_rect()[2]//2
        self.bet_100_y=self.screen.get_rect()[3]*3//5 + self.bet_100.get_rect()[3]//4
        
        self.bet_200_x=self.screen.get_rect()[2]*4//8 - self.bet_200.get_rect()[2]//2
        self.bet_200_y=self.screen.get_rect()[3]*3//5 - self.bet_200.get_rect()[3]//4
        
        self.bet_500_x=self.screen.get_rect()[2]*6//8 - self.bet_500.get_rect()[2]//2
        self.bet_500_y=self.screen.get_rect()[3]*3//5 + self.bet_500.get_rect()[3]//4
 
        self.bet_reset_x=self.screen.get_rect()[2]*7//8 - self.bet_reset.get_rect()[2]//2
        self.bet_reset_y=self.screen.get_rect()[3]*3//5

        
        ''' Card Game elements'''
        
        self.play_hit=pygame.image.load("Pictures/Hit.png")
        self.play_double=pygame.image.load("Pictures/Double.png")            
        self.play_stand=pygame.image.load("Pictures/Stand.png")

        self.play_hit_x = int(self.screen_rect.center[0]//2-self.play_hit.get_rect()[2]//2)
        self.play_hit_y = int(self.screen_rect.center[1]*1.5)

        self.play_double_x = int(self.screen_rect.center[0]-self.play_double.get_rect()[2]//2)
        self.play_double_y = int(self.screen_rect.center[1]*1.6)

        self.play_stand_x = int(self.screen_rect.center[0]*1.5-self.play_stand.get_rect()[2]//2)
        self.play_stand_y = int(self.screen_rect.center[1]*1.5)
        
        if self.settings.intro==True:
            self.screen.fill ( self.settings.bg_color_intro_game )
            

            
            self.screen.blit ( self.intro_text_1,
                                   ( self.settings.screen_rect.center[0] - self.intro_text_1.get_rect ()[2]/2
                                    ,self.settings.screen_rect.center[1]/3 - self.intro_text_1.get_rect ()[3]/2))
            
            self.screen.blit ( self.intro_text_2,
                                   ( self.settings.screen_rect.center[0] - self.intro_text_2.get_rect ()[2]/2
                                    ,self.settings.screen_rect[3]-self.settings.screen_rect.center[1]*1/3 - self.intro_text_2.get_rect ()[3]/2))
            
            self.screen.blit ( self.intro_play,
                                   ( self.settings.screen_rect[2]/5  - self.intro_play.get_rect ()[2]/2
                                    ,self.settings.screen_rect.center[1] - self.intro_play.get_rect ()[3]/2))
            
            self.screen.blit ( self.intro_quit,
                                   ( self.settings.screen_rect[2]*4/5 - self.intro_quit.get_rect ()[2]/2
                                    ,self.settings.screen_rect.center[1] - self.intro_quit.get_rect ()[3]/2))

            self.screen.blit ( self.intro_cards,
                                   ( self.settings.screen_rect.center[0] - self.intro_cards.get_rect ()[2]/2
                                    ,self.settings.screen_rect.center[1] - self.intro_cards.get_rect ()[3]/2))

        if self.settings.bet_stage==True:

            self.screen.fill(self.settings.bg_color_bet_game)
            
            self.screen.blit(self.bet_text,
                                 (self.screen_rect.center[0]-self.bet_text.get_rect()[2]/2,
                                  self.screen.get_rect()[3]/5))
            
            self.screen.blit(self.bet_bankroll,
                                 (self.screen_rect.center[0]-self.bet_bankroll.get_rect()[2]/2,
                                  self.screen.get_rect()[3]*2/5))
            
            self.screen.blit(self.bet_bet,
                                 (self.screen_rect.center[0]-self.bet_bet.get_rect()[2]/2,
                                  self.screen.get_rect()[3]*2/5+self.settings.space_y))
            

            
            self.screen.blit(self.bet_done,
                                 (self.bet_done_x,
                                  self.bet_done_y))
            
            self.screen.blit(self.bet_100,
                                 (self.bet_100_x,
                                  self.bet_100_y))
            
            self.screen.blit(self.bet_200,
                                 (self.bet_200_x,
                                  self.bet_200_y))
            
            self.screen.blit(self.bet_500,
                                 (self.bet_500_x,
                                  self.bet_500_y))
            
            self.screen.blit(self.bet_reset,
                                 (self.bet_reset_x,
                                  self.bet_reset_y))
            
     
        if self.settings.play_stage==True:
            if self.playerscreen.points_cards==21:
                self.computerscreen.stage="Dealer"
                

            
            
            
            self.screen.fill(self.settings.bg_color_card_game)
            self.playerscreen.blitme()
            self.computerscreen.blitme()
            
            self.screen.blit(self.play_hit,(self.play_hit_x,
                                            self.play_hit_y))
            if self.settings.player_hit==False:
                self.screen.blit(self.play_double,(self.play_double_y,
                                                self.play_double_y))
            
            
            self.screen.blit(self.play_stand,(self.play_stand_x,
                                            self.play_stand_y))
            
            
            if self.computerscreen.stage=="Dealer":
                if self.computerscreen.points_cards<17:
                    self.computerscreen.hit_card()
                if self.computerscreen.points_cards>16:
                    self.settings.play_stage=False
                    self.settings.end_stage=True
                    
                    
        if self.settings.end_stage==True:
            self.screen.fill((self.settings.bg_color_end_stage))
            self.screen_rect=self.screen.get_rect()
            
            self.lost_text=self.settings.font.render("Sorry, you lost this hand! Press R to play a new hand or Q to exit!",True,(0,0,0))
            self.win_text=self.settings.font.render(f"Congratulations, you won {self.settings.current_bet} coins! Press R to play a new hand or Q to exit!",True,(0,0,0))
            self.playerscreen.blitme()
            self.computerscreen.blitme()
            if self.settings.over_21==True or (self.playerscreen.points_cards<=self.computerscreen.points_cards and self.computerscreen.points_cards<22):
                self.screen.blit(self.lost_text,(self.screen_rect.center[0],self.screen_rect.center[1]-self.lost_text.get_rect()[3]//2))
                self.settings.bankroll-=self.settings.current_bet
                self.settings.end_stage=False
            if (self.playerscreen.points_cards>self.computerscreen.points_cards and self.settings.over_21==False) or (self.playerscreen.points_cards<22 and self.computerscreen.points_cards>21):
                self.screen.blit(self.win_text,(self.screen_rect.center[0],self.screen_rect.center[1]-self.win_text.get_rect()[3]//2))
                self.settings.bankroll+=self.settings.current_bet
                self.settings.end_stage=False

        # Make the most recently drawn screen visible
        pygame.display.flip()    


    def _redeal_hand(self):
        self.settings.bet_stage = True
        self.settings.end_stage = self.settings.over_21 = False
        self.computerscreen.remake_cards()
        self.playerscreen.remake_cards()
        self.computerscreen.stage="Player"
        self.settings.current_bet=0
        self.settings.player_hit=False
        if self.settings.bankroll<=0:
            self.settings.bankroll=1000


if __name__=='__main__':
    bj=BlackJack()
    bj.run_game()
