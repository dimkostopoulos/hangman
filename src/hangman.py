import random

#TODO Add greek

words = ['python', 'java', 'hangman', 'computer', 'keyboard', 'programming', 'panileiakos']
word = random.choice(words).lower()
word_letters = set(word)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
used_letters = set()
lives = 9

# Game loop
while len(word_letters) > 0 and lives > 0:
	print(f'\nYou have {lives} lives left')
	print('Used letters:', ' '.join(used_letters))
	
	# Show current word progress
	word_list = [letter if letter in used_letters else '_' for letter in word]
	print('Current word:', ' '.join(word_list))
	
	user_letter = input('Guess a letter poser: ').lower()
	
	if user_letter in alphabet - used_letters:
		used_letters.add(user_letter)
		if user_letter in word_letters:
			word_letters.remove(user_letter)
		else:
			lives -= 1
			print('Letter is not in word loser!')
	
	elif user_letter in used_letters:
		print('You already used that letter!')
	else:
		print('Invalid character!')

# Game over
if lives == 0:
	print(f'\nYou died bitch! The word was: {word}')
else:
	print(f'\nCongratulations! You guessed the word: {word}')

