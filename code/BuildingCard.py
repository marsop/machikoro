class BuildingCard(Card):
	"""Represents a normal building card in the game"""
	def __init__(self, title, cost, card_type, dice_results, reward):
		Card.__init__(self, title, cost, card_type)
		self.dice_results = dice_results
		self.reward = reward
		
	def activate(self, player, result):
		roll = sum(result)
		if (roll in self.dice_results):
			player.take_coins(self.reward)
