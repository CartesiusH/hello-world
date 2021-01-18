from random import choice

#Program decides on word and gives spaces
guesses = 0
correct = []
myWords = ['waterbottle','highway','pillow']
chosenword = choice(myWords)
print(len(chosenword)*'_ ')
print('')

#Program takes a guess from the user
while guesses <= 10:
	letter = input()
	i = 0
	finished = True # Will become false when '_' is printed or wrong guess is made.
	
	if letter in chosenword: # Seeing if what they entered is correct.
		correct.append(letter)
		print('You guessed right!')
		
		while (i < len(chosenword)): # Printing everything they have so far.
			if chosenword[i] in correct:
				print(chosenword[i],' ',end='')
			else:
				print('_ ',end='')
				finished = False
			i = i + 1
		
		print('')
		print('')
		if finished == True: print('Congratulations! You won!')
	
	else: 
		if guesses < 10:
			finished = False
			print ('Sorry, try again! You have',10-guesses,'guesses left!')
			print('')
		else:
			print('Sorry, you are out of guesses! Game over!')
	
	guesses = guesses + 1






