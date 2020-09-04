import random
import pygame


class Cards:
    def __init__(self, game, player):
        self.game = game
        self.gameScreen = game.screen
        self.gameRect = self.gameScreen.get_rect()
        self.player = player
        self.playerTurn = True

        '''
        Here, we create a dictionary which contains each of the 52 cards 
        available in a deck (along with a pair of 4 Small Acess) and the 
        corresponding point value for each card
        '''
        self.cards = ["Asmall"] + list(range(2, 11)) + ["J", "Q", "K", "A"]
        self.cardSuits = ["HEARTS", "DIAMONDS", "SPADES", "CLUBS"]
        self.points = sorted((list(range(1, 12)) + [10] * 3) * 4)
        self.cardDeck = [
            f"{i} of {j}" for i in self.cards for j in self.cardSuits
        ]
        self.pointsDict = {
            i:self.points[self.cardDeck.index(i)] for i in self.cardDeck
        }


    def dealHand(self):
        self.cardPoints = 0
        self.playerCards = [
            self.cardDeck[random.randint(4, 55)],
            self.cardDeck[random.randint(4, 55)]
        ] 
    

    def hit_card(self):
        self.playerCards.append(self.cardDeck[random.randint(4, 55)])

    
    def blitme(self):
        self.cardPoints = sum([self.pointsDict[eachCard] for eachCard in self.playerCards])
        
        # Attribute a value of 1 to one Ace card in case player has over 21
        if self.cardPoints > 21:
            for each_card in self.playerCards:
                if "A of" in each_card:
                    self.cardPoints -= 10
                    self.playerCards[self.playerCards.index(each_card)].replace("A of", "Asmall of")
                    break

        self.cardsList = [
            "assets/cards/" + eachCard + ".png" for eachCard in self.playerCards
            ]   
     
        if self.playerTurn and self.player == "Dealer":
            self.textMessage = " has at least "
            self.cardPoints = self.pointsDict[self.playerCards[0]]
        else:
            self.textMessage = " has "

        if self.player == "Player":
            self.cardsPosition = [(self.gameRect[2]//3 + i*100, self.gameRect[3]//2) for i in range(len(self.cardsList))]
        else: 
            self.cardsPosition = [(self.gameRect[2]//3 + i*100, self.gameRect[3]//9) for i in range(len(self.cardsList))]

        for eachCard in self.cardsList:
            self.cardImage = pygame.image.load(eachCard)
            self.gameScreen.blit(
                self.cardImage, 
                self.cardsPosition[self.cardsList.index(eachCard)]
            )
            if self.player == "Dealer" and self.playerTurn: break

        self.text = self.game.settings.font.render(
            f" {self.player} {self.textMessage} {self.cardPoints} points!",
            True,
            self.game.settings.textColor
        )

        if self.player == "Player":
            self.gameScreen.blit(self.text, (
                self.gameRect.center[0] - self.text.get_rect()[2],
                self.gameRect[3] * 3 // 4
                )
            )
        else:
            self.gameScreen.blit(self.text,(
                self.gameRect.center[0]-self.text.get_rect()[2],
                self.gameRect[3]//12))
