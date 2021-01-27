import random
import cards 

class Game:

    def __init__(self, players, is_verbose=False):

        self.is_verbose = is_verbose
        self.players = players
        for player in players:
            player.game = self

        self.unplayed_cards = cards.generateSuit()

        self.upcard = None


    def _playRound(self):
        if self.is_verbose:
            print(f'Round {14 - len(self.unplayed_cards)}')

        self.upcard = random.choice(self.unplayed_cards)

        for player in self.players:
            player.pickCard()

        # Find winner(s)
        highest_card = -1
        highest_players = []

        for player in self.players:
            if self.is_verbose:
                print(f'{player.name} played {cards.names[player.played_card]}')

            if player.played_card == highest_card:
                highest_players.append(player)

            elif player.played_card > highest_card:
                highest_card = player.played_card
                highest_players = [player]

            player.unplayed_cards.remove(player.played_card)

        # Update winner(s) score
        if self.is_verbose:
            print("Winner(s): ", end="")
        for player in highest_players:
            if self.is_verbose:
                print(player.name, end=" ")
            player.score += self.upcard + 1 # Cards are 0-indexed, so add one
        
        if self.is_verbose:
            print("\n")

        self.unplayed_cards.remove(self.upcard)
        

    def play(self):
        for _ in range(13):
            self._playRound()


    def reset(self):
        self.unplayed_cards = cards.generateSuit()
        for player in self.players:
            player.reset()


    def printScores(self):
        print("Scores:")
        for player in self.players:
            print(f'{player.name}\t{player.score}')


if __name__ == '__main__':
    import approaches

    g = Game([approaches.PlusOne("+1"), approaches.Human("Jacob")], is_verbose=True)

    g.play()

    g.printScores()