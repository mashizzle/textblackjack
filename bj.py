import random

suit = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
rank = {'ACE': 11, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10, 'JACK': 10, 'QUEEN': 10, 'KING': 10}


# Represents the card class with the suit and type of card
class Card():
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val

	def show(self):
		print(self.val, 'of', self.suit)
		

# The deck of cards, that can be built, shuffled and drawn from.
class Deck():
	

	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		
		for i in suit:
			for j in rank:
				self.cards.append(Card(i,j))

	def show(self):
		for c in self.cards:
			c.show()

	def shuffle(self):
		random.shuffle(self.cards)

	def drawCard(self):
		return self.cards.pop()


# Represents a player who can draw cards and hold a hand
class Player():
	def __init__(self):
		self.hand = []
		self.bet = 0

	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self.hand

	def showHand(self):
		for c in self.hand:
			c.show()

# Represents the dealer subclass of player that can show all cards except one
class Dealer(Player):

	def showPartHand(self):
		for c in self.hand[1:]:
			c.show()
		

# Game loop
def blackJack():
	d1 = Deck()
	d1.shuffle()
	player = Player()
	dealer = Dealer()
	print('Player has:')
	player.drawCard(d1)
	dealer.drawCard(d1)
	player.drawCard(d1)
	dealer.drawCard(d1)

	player.showHand()
	print('_________')
	print('Dealer has:')
	dealer.showPartHand()

	pCardSum = 0
	dCardSum = 0
	
	# Sums up the starting hand of the player
	for c in player.hand:
		pCardSum = pCardSum + rank[c.val]


	# Sums up the starting hand of the dealer
	for c in dealer.hand:
		dCardSum = dCardSum + rank[c.val]

	# If the player has 21 on starting hand they win
	if pCardSum == 21:
		print('Black Jack! You win!')
	else:
		# empty list to contain index positions of ACES
		acePos = []
		turn = True
		while pCardSum < 21 and turn:
			move = input('Enter "h" for another card, or "c" to check:  ')
			if move == 'h':
				print('_________')
				player.drawCard(d1)
				player.showHand()

				# Creates a copy of the latest card dealt
				pTempCard = player.hand[len(player.hand)-1]

				pCardSum = pCardSum + rank[pTempCard.val]

				# Loop to lower the value of an ACE to 1 if total sum of cards is over 21
				# and if the index position of ACE has not been entered into acePos list.

				if pCardSum > 21:
					for pos in range(len(player.hand)):
						if player.hand[pos].val == 'ACE' and pos not in acePos and pCardSum > 21:
							acePos.append(pos)
							print(player.hand[pos].val)
							pCardSum = pCardSum - 10




				
				print(pCardSum)
			elif move == 'c':
				turn = False
		if pCardSum > 21:
			print('Bust, you lose!')

		if pCardSum <=21:
			acePosD = []
			while dCardSum < 17:

				dealer.drawCard(d1)
				dTempCard = dealer.hand[len(dealer.hand)-1]
				dCardSum = dCardSum + rank[dTempCard.val]

				if dCardSum > 21:
					for pos in range(len(dealer.hand)):
						if dealer.hand[pos].val == 'ACE' and pos not in acePosD and dCardSum > 21:
							acePosD.append(pos)
							dCardSum = dCardSum - 10

				print(dCardSum)

			if dCardSum > 21:
				dealer.showHand()
				print('Dealer bust, you win!')
			elif pCardSum > dCardSum:
				dealer.showHand()
				print('You win!')
			elif pCardSum == dCardSum:
				dealer.showHand()
				print("Split! It's a draw")
			else:
				dealer.showHand()
				print('Dealer wins!')





	



blackJack()






