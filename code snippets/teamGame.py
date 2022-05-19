# The player starts the game with 300 points.
# Individual cards are represented as a number from 1 to 13.
# The current card is displayed.
# The player guesses if the next one will be higher or lower.
# The the next card is displayed.
# The player earns 100 points if they guessed correctly.
# The player loses 75 points if they guessed incorrectly.
# If a player reaches 0 points the game is over.
# If a player has more than 0 points they decide if they want to keep playing.
# If a player decides not to play again the game is over.

class Director:
	def __init__(self):
		self.cards= []
		self.is_playing = True
		self.score = int()
		self.total_score = int()

	def get_started(self):
		while self.is_playing:
			self.get_inputs()
			self.update_game()
			self.game_output()

	def update_game(self):
		if not self.is_playing:
			print("Thanks for playing!\nBetter luck next time...")
			return

		for i in range(len(self.cards)):
			card = self.cards[i]
			card.compare()
			self.score += card.points
		self.total_score += self.score