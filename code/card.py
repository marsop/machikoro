class CardType:
	BLUE = 1    
	GREEN = 2	
	RED = 3
	PURPLE = 4
	GOLDEN = 5

class Card:
	"""Represents a card in the game"""
	def __init__(self, title, cost, card_type, dice_results, reward, is_unique):
		self.title = title
		self.cost = cost
		self.card_type = card_type
		self.dice_results = dice_results
		self.reward = reward
		self.is_unique = is_unique
		print "new card " + title + " created" 
		
		
class GoldenCard:
	"""Represents one of the victory cards"""
	def __init__(self, title, cost, card_type):
		self.title = title
		self.cost = cost
		self.card_type = card_type