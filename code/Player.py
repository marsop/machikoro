from card import CardName
import abc

class Player(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self, name):
		self.name = name
		self.playing_area = []
		self.coins = 0
		
	def buy_card(self, card):
		self.coins -= card.cost
		self.playing_area.append(card)
		#print "player " + self.name + " has bought card " + card.card_name + " ("+ str(self.coins)+" coins left)"
		
	def take_coins(self, amount):
		self.coins += amount
		#print "player " + self.name + " has now " + str(self.coins) + " coins"
		
	def has(self, card_name):
		result = [x for x in self.playing_area if x.card_name == card_name]
		return len(result) != 0
		
	def has_all_gold_cards(self):
		return self.has(CardName.TRAIN_STATION) and self.has(CardName.SHOPPING_MALL) and self.has(CardName.AMUSEMENT_PARK) and self.has(CardName.RADIO_TOWER)
		
	@abc.abstractmethod
	def choose_action(self, game):
		"""Decides which action to take"""
		return
