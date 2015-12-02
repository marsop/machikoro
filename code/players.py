from player import Player
from card import CardName

class DoNothingPlayer(Player):
	def choose_action(self, game):
		return None
	
class BuyGoldenPlayer(Player):
	def choose_action(self, game):
		if ((not self.has(CardName.TRAIN_STATION)) and self.coins > 4 ):
			return CardName.TRAIN_STATION
		if ((not self.has(CardName.SHOPPING_MALL)) and self.coins > 10 ):
			return CardName.SHOPPING_MALL
		if ((not self.has(CardName.AMUSEMENT_PARK)) and self.coins > 16 ):
			return CardName.AMUSEMENT_PARK
		if ((not self.has(CardName.RADIO_TOWER)) and self.coins > 22 ):
			return CardName.RADIO_TOWER
		else:
			return None
			
class BuyGoldenExactPlayer(Player):
	def choose_action(self, game):
		if ((not self.has(CardName.TRAIN_STATION)) and self.coins >= 4 ):
			return CardName.TRAIN_STATION
		if ((not self.has(CardName.SHOPPING_MALL)) and self.coins >= 10 ):
			return CardName.SHOPPING_MALL
		if ((not self.has(CardName.AMUSEMENT_PARK)) and self.coins >= 16 ):
			return CardName.AMUSEMENT_PARK
		if ((not self.has(CardName.RADIO_TOWER)) and self.coins >= 22 ):
			return CardName.RADIO_TOWER
		else:
			return None