# blackjack

A simple Python simulation for blackjack, allowing you to test different strategies by creating a new player and defining their strategy.

A new player is created by subclassing the Player class and then implementing the abstract should_hit method:

```python
@abstractmethod
def should_hit(self):
    pass
```

For example:

```python
class BasicPlayer(Player):

    def should_hit(self):
        return self.hand.score() <= 10
```

To run it, simply add new players to simulation.py:

```python
game = games.Game()
game.add_player(players.BasicPlayer('Basic Player 1'))
game.add_player(players.SmartPlayer('Smart Player 1'))
```

And then run the simulation:

```python
python simulations.py
```
