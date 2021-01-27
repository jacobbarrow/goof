import random

import cards

from player import Player

class Random(Player):
    # Picks a card at random
    def pickCard(self):
        self.played_card = random.choice(self.unplayed_cards)


class PlusOne(Player):
    # Picks the card one higher than the upcard
    def pickCard(self):
        # For king, bet ace
        if self.game.upcard == 12: 
            self.played_card = 0
        else:
            self.played_card = self.game.upcard + 1


class Human(Player):
    # Lets a user pick the card
    def pickCard(self):
        print(f'The upcard is {cards.names[self.game.upcard]}')
        print(f'Your unplayed cards are {cards.namedList(self.unplayed_cards)}')

        self.played_card = None
        print('Pick a card!')
        while self.played_card is None:
            raw_pick = input('>> ')            
            if raw_pick in cards.namedList(self.unplayed_cards):
                self.played_card = cards.names.index(raw_pick)
            else:
                print("That's not in your unplayed cards, pick another")
            
