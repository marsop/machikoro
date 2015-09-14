class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
		
	def take_card(self, card):
		self.hand.append(card)
		print "player " + self.name + " has taken card " + card.title