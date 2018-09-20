from abc import ABC, abstractmethod

class PlayerStrategyAbstract(ABC):

	@abstractmethod
	def should_hit(self):
		pass
		
		
class DealerStrategy(PlayerStrategyAbstract):

	def should_hit(self):
		return True
	
	
	
	
	
if __name__ == '__main__':
	p = Player()