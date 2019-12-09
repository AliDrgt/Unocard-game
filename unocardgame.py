
#CODED BY ALİ FATİH DURGUT#

import random
import time

class UnoCards:
    def __init__(self,color,number):
        self.color = color
        self.number = number

    def canCardPlay(self,other):
        if other.color == self.color or other.number == self.number:
            return True
        return False

    def __str__(self):
        return self.color + str(self.number)

class CollectionOfUnoCards:
    def __init__(self):
       self.deck = []

    def addCards(self, card):
        self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def removeCard(self,card):
        self.deck.remove(card)

    def removeCardbyIndex1(self,index):
        self.deck.pop(index)

    def getNumCards(self):
        return len(self.deck)

    def getTopCard(self):
        return self.deck[0]

    def getCard(self, index):
        return self.deck[index]

    def findCard(self, c):
        c_color, c_num = c.split(',')
        for i, card in enumerate(self.deck):
            color, num = card.split(',')
            if (color == c_color or num == c_num):
                return i

    def canPlay(self,other):
        for i in range(deck.getNumCards()):
            for card in self.deck:
                if card.color == other.color or card.number==other.number :
                    return True
        return False

    def thenPlay(self,other):
        for i in range(deck.getNumCards()):
            for card in self.deck:
                if card.color == other.color or card.number==other.number :
                    return card

    def makeDeck(self):
        for num in range(1,10):
            for color in ("Yellow","Green","Blue","Red"):
                card = UnoCards(color, num)
                deck.addCards(card)
                deck.addCards(card)

    def __str__(self):
        col_str = ""
        for i in range(0,len(self.deck)):
            col_str = col_str + " " + str(self.deck[i])
        return col_str

deck = CollectionOfUnoCards()
hand1 = CollectionOfUnoCards()
hand2 = CollectionOfUnoCards()
deck.makeDeck()
deck.shuffle()

class Uno:

    def cardSpread(self):
        for i in range(7):
            hand1.addCards(deck.getCard(0))
            deck.removeCard(deck.getCard(0))
            hand2.addCards(deck.getCard(0))
            deck.removeCard(deck.getCard(0))

    def playUno(self):
        lastPlayedCard = deck.getTopCard()
        deck.removeCardbyIndex1(0)
        print("Opened card: ",lastPlayedCard)
        while True:

            if hand1.canPlay(lastPlayedCard)==True:
                a = hand1.thenPlay(lastPlayedCard)
                time.sleep(1)
                print("Player 1's deck----", hand1,"        ",lastPlayedCard,"         ",hand2,"----Player2's deck")
                hand1.removeCard(hand1.thenPlay(lastPlayedCard))
                lastPlayedCard = a
                time.sleep(2)
                print("                              ""Player 1 played: ",lastPlayedCard,"\n")
                if hand1.getNumCards()==0:
                    print("Player 1 Win")
                    print("Cards left in deck= ", deck.getNumCards())
                    break

                if hand1.getNumCards()==1:
                    print("UNO!!!")

            elif hand1.canPlay(lastPlayedCard)==False:
                hand1.addCards(deck.getTopCard())
                time.sleep(2)
                print("                             ""Player 1 draw a card","\n")
                deck.removeCardbyIndex1(0)

            if deck.getNumCards()==0:
                deck.makeDeck()
                deck.shuffle()
                print("Deck refreshed")

            if hand2.canPlay(lastPlayedCard)==True:
                b = hand2.thenPlay(lastPlayedCard)
                time.sleep(1)
                print("Player 1's deck----", hand1,"       ",lastPlayedCard,"       ",hand2,"----Player2's deck")
                hand2.removeCard(hand2.thenPlay(lastPlayedCard))
                lastPlayedCard = b
                time.sleep(2)
                print("                                                                       ", lastPlayedCard," :Player 2 played","\n")
                if hand2.getNumCards() == 0:
                    print("Player 2 Win")
                    print("Cards left in deck= ",deck.getNumCards())
                    break
                if hand2.getNumCards()==1:
                    print("                                                                        UNO!!!")


            elif hand2.canPlay(lastPlayedCard)==False:
                hand2.addCards(deck.getTopCard())
                time.sleep(2)
                print("                                                                        ""Player 2 draw a card","\n")
                deck.removeCardbyIndex1(0)

mygame = Uno()
mygame.cardSpread()
mygame.playUno()

