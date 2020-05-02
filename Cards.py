import random
import pygame
from settings import Settings



class Cards:
    def __init__(self,screen,player):
        ### Initialize flags and other variables
        self.player=player
        self.stage="Player"
        self.hit_hit=False
        self.points_cards=0


        ### Create a dictionary with each card and its corresponding number of points
        self.all_cards=[]
        self.points={}
        self.cards=["Asmall",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        self.nr_points=sorted([1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4)
        self.colours=["HEARTS","DIAMONDS","SPADES","CLUBS"]

        for i in self.cards:
            for j in self.colours:
                self.all_cards.append(f"{i} of {j}")

        for i in self.all_cards:
            self.points[i]=self.nr_points[self.all_cards.index(i)]    
        
        
        ### DEAL A SET OF RANDOM CARDS
        self.player_cards= [
            self.all_cards[random.randint(4,55)],self.all_cards[random.randint(4,55)]]
         
        self.screen=screen.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=Settings(self)
        


    def remake_cards(self):
        self.points_cards=0
        self.player_cards= [
            self.all_cards[random.randint(4,55)],self.all_cards[random.randint(4,55)]]       

    def show_cards(self):
        print(self.player_cards)
    
    def hit_card(self):
#        if self.hit_hit==True:
        self.player_cards.append(self.all_cards[random.randint(0,51)])

    
    
    def blitme(self):
        self.points_cards=0
        for each_card_in_hand in self.player_cards:
            self.points_cards+=self.points[each_card_in_hand]
            
        if self.points_cards>21:
            i=0
            for each_card in self.player_cards:
                if "A of" in each_card:
                    self.points_cards-=10
                    self.player_cards[i]=self.player_cards[i].replace("A of","Asmall of")
                    break
                i+=1
                    
        
        self.list_of_cards=[]
        self.position_of_cards=[]
        

        
        
        if self.player=="Player":
            for each_card in self.player_cards:
                self.x="Pictures/All_cards/"+each_card+".png"
                self.list_of_cards.append(self.x)

            
            for i in range(len(self.list_of_cards)):
                self.y=(self.screen_rect[2]//3+i*100,self.screen_rect[3]//2)
                self.position_of_cards.append(self.y)

            
            for md in self.list_of_cards:
                self.xyz=pygame.image.load(md)
                self.screen.blit(self.xyz,self.position_of_cards[self.list_of_cards.index(md)])
            
            
            self.text=self.settings.font.render(
                f" {self.player} has {self.points_cards} points!",
                True, (255, 255, 255)
                )
            
            self.screen.blit(self.text,(
                self.screen_rect.center[0]-self.text.get_rect()[2]
                ,self.screen_rect[3]*3//4))
           
           




        if self.player=="Dealer":
          
            for each_card in self.player_cards:
                self.x="Pictures/All_cards/"+each_card+".png"
                self.list_of_cards.append(self.x)

            
            for i in range(len(self.list_of_cards)):
                self.y=(self.screen_rect[2]//3+i*100,self.screen_rect[3]//9)
                self.position_of_cards.append(self.y)            
            
            if self.stage=="Player":
                self.text2=self.settings.font.render(
                    f" {self.player} has at least {self.points[self.player_cards[0]]} points!",
                    True, (255, 255, 255)
                    )
                
                self.screen.blit(self.text2,(
                    self.screen_rect.center[0]-self.text2.get_rect()[2],
                    self.screen_rect[3]//12))
                
                self.xyz=pygame.image.load(self.list_of_cards[0])
                self.screen.blit(self.xyz,self.position_of_cards[0])
                
            else:
                self.text2=self.settings.font.render(
                    f" {self.player} has {self.points_cards} points!",
                    True, (255, 255, 255)
                    )
                
                self.screen.blit(self.text2,(
                    self.screen_rect.center[0]-self.text2.get_rect()[2],
                    self.screen_rect[3]//12))
                


            
                for md in self.list_of_cards:
                    self.xyz=pygame.image.load(md)
                    self.screen.blit(self.xyz,self.position_of_cards[self.list_of_cards.index(md)])  