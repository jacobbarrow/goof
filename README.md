# Goof


## Add your own approach

To add your own approach, add a class to `approaches.py` that inherits the Player class, and has a method `pickCard` that sets `self.played_card` to the zero-indexed value of the card (A=0, K=12).

 There's a few variables available:

```python
class MyCoolApproach(Player):
    def pickCard(self):
        # The current upcard to bid against
        self.game.upcard 

        # The cards you've not yet played
        self.unplayed_cards 

        # A list of all players in the game
        self.game.players

        # Player index x's unplayed cards
        self.game.players[x].unplayed_cards 

        self.played_card = # The card to bet
```

Then, to test it out, add the approach to the list in `main.py`, passing a name as an argument, and run it

```python
players = approaches.MyCoolApproach("Bob")
```
