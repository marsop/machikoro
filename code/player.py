class Player:
	def __init__(self, name):
		self.name = name
		self.playing_area = []
		self.coins = 0
		
	def buy_card(self, card):
		self.coins -= card.cost
		self.playing_area.append(card)
		print "player " + self.name + " has taken card " + card.title + " (coins left "+ str(self.coins)+")"
		
	def add_card(self, card):
		self.playing_area.append(card)
		print "player " + self.name + " has taken card " + card.title + " (coins left "+ str(self.coins)+")"
		
	def take_coins(self, amount):
		self.coins += amount
		print "player " + self.name + " has now " + str(self.coins) + " coins"