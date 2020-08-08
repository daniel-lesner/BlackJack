import random
import pygame


class Cards:
    def __init__(self, game, player):
        ### Initialize flags and other variables
        self.game = game
        self.player = player
        self.stage = "Player"
        self.hit_hit = False
        self.cardPoints = 0


        ### Create a dictionary with each card and its corresponding number of points
        self.all_cards = []
        self.points = {}
        self.cards = ["Asmall"] + list(range(2,11)) +["J","Q","K","A"]
        self.nr_points = sorted((list(range(1,12)) + [10] * 3) * 4)
        self.colours = ["HEARTS","DIAMONDS","SPADES","CLUBS"]

        for i in self.cards:
            for j in self.colours:
                self.all_cards.append(f"{i} of {j}")

        for i in self.all_cards:
            self.points[i]=self.nr_points[self.all_cards.index(i)]    
        
        
        ### DEAL A SET OF RANDOM CARDS
        self.player_cards= [
            self.all_cards[random.randint(4, 55)],
            self.all_cards[random.randint(4, 55)]
            ]
         
        self.gameScreen = game.screen
        self.gameRect=self.gameScreen.get_rect()
        

    def remake_cards(self):
        self.cardPoints=0
        self.player_cards= [
            self.all_cards[random.randint(4, 55)],
            self.all_cards[random.randint(4, 55)]]       


    def show_cards(self):
        print(self.player_cards)
    

    def hit_card(self):
        # if self.hit_hit==True:
        self.player_cards.append(self.all_cards[random.randint(0,51)])

    
    def blitme(self):
        self.cardPoints=0
        for each_card_in_hand in self.player_cards:
            self.cardPoints+=self.points[each_card_in_hand]
            
        if self.cardPoints > 21:
            i = 0
            for each_card in self.player_cards:
                if "A of" in each_card:
                    self.cardPoints-=10
                    self.player_cards[i]=self.player_cards[i].replace("A of","Asmall of")
                    break
                i += 1
                    
        
        self.list_of_cards=[]
        self.position_of_cards=[]
        
     
        if self.player == "Player":
            for each_card in self.player_cards:
                self.x="assets/cards/"+each_card+".png"
                self.list_of_cards.append(self.x)

            
            for i in range(len(self.list_of_cards)):
                self.y=(self.gameRect[2]//3+i*100,self.gameRect[3]//2)
                self.position_of_cards.append(self.y)

            
            for md in self.list_of_cards:
                self.xyz=pygame.image.load(md)
                self.gameScreen.blit(self.xyz,self.position_of_cards[self.list_of_cards.index(md)])
            
            
            self.text=self.game.settings.font.render(
                f" {self.player} has {self.cardPoints} points!",
                True, self.game.settings.textColor
                )
            
            self.gameScreen.blit(self.text,(
                self.gameRect.center[0]-self.text.get_rect()[2]
                ,self.gameRect[3]*3//4)
                )
           
           
        if self.player=="Dealer":
          
            for each_card in self.player_cards:
                self.x="assets/cards/"+each_card+".png"
                self.list_of_cards.append(self.x)

            
            for i in range(len(self.list_of_cards)):
                self.y=(self.gameRect[2]//3+i*100,self.gameRect[3]//9)
                self.position_of_cards.append(self.y)            
            
            if self.stage=="Player":
                self.text2=self.game.settings.font.render(
                    f" {self.player} has at least {self.points[self.player_cards[0]]} points!",
                    True, self.game.settings.textColor
                    )
                
                self.gameScreen.blit(self.text2,(
                    self.gameRect.center[0]-self.text2.get_rect()[2],
                    self.gameRect[3]//12))
                
                self.xyz=pygame.image.load(self.list_of_cards[0])
                self.gameScreen.blit(self.xyz,self.position_of_cards[0])
                
            else:
                self.text2=self.game.settings.font.render(
                    f" {self.player} has {self.cardPoints} points!",
                    True, self.game.settings.textColor
                    )
                
                self.gameScreen.blit(self.text2,(
                    self.gameRect.center[0]-self.text2.get_rect()[2],
                    self.gameRect[3]//12))
                


            
                for md in self.list_of_cards:
                    self.xyz=pygame.image.load(md)
                    self.gameScreen.blit(self.xyz,self.position_of_cards[self.list_of_cards.index(md)])  