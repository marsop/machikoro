class CardType:
	BLUE = 1    
	GREEN = 2	
	RED = 3
	PURPLE = 4
	GOLDEN = 5

class Card:
	def __init__(self, title, cost, card_type):
		"""Represents a card in the game"""
		self.title = title
		self.cost = cost
		self.card_type = card_type
		print "new card " + title + " created" 

class BuildingCard(Card):
	"""Represents a normal building card in the game"""
	def __init__(self, title, cost, card_type, dice_results, reward, only_one_allowed):
		Card.__init__(self, title, cost, card_type)
		self.dice_results = dice_results
		self.reward = reward
		self.only_one_allowed = only_one_allowed
		
class VictoryCard(Card):
	"""Represents one of the victory cards"""
	def __init__(self, title, cost, card_type, built):
		Card.__init__(self, title, cost, card_type)
		self.built = built