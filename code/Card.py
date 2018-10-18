class Card:
	def __init__(self, card_name, cost, card_type):
		"""Represents any card in the game"""
		self.card_name = card_name
		self.cost = cost
		self.card_type = card_type
		
	# Indicates how many cards can the user have w.r.t. Card Type
	def get_maximum_number_per_player(card_type):
		return 1 if card_type == PURPLE or card_type == GOLDEN else -1
			
	def is_active(self, owner, active_player):
		if (owner == active_player):
			return (self.card_type == PURPLE or self.card_type == BLUE or self.card_type == GREEN or self.card_type == GOLDEN)
		else:
			return (self.card_type == RED or self.card_type == BLUE)
