# blackjack

A simple Python simulation for blackjack games, originally written to help me jump back into Python. It started off as a very simple console game, which can be run by using:

```python
python main.py
```

Or you can run simulations to test various strategies by running:

```python
python simulations.py
```

In each you can add any number of players besides the dealer, with each player type being a subclass of a Player class. Player has one abstract method:

```python
@abstractmethod
def should_hit(self):
    pass
```

A player can be very generic (and likely not very good):

```python
class BasicPlayer(Player):

    def should_hit(self):
        return self.hand.score() <= 10
```

Or they can be a bit more sophisticated and base their hit/stay on factors such as all face up cards on the table, some memory of the last couple of rounds, etc.
