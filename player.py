import cards

class Player:
    def __init__(self, name):
        self.name = name
        self.game = None
        self.reset()


    def playCard(self):
        self.unplayed_cards.remove(self.played_card)

    
    def reset(self):
        self.unplayed_cards = cards.generateSuit()
        self.played_card = None
        self.score = 0