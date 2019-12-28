def guess_me(goal_string):
	stuff = list(goal_string.lower())
	display = ['_' if letter.isalpha() else letter for letter in stuff]
    
	game_on = True
	while game_on:
		print("--> {}".format(" ".join(display)))
		inp_letter = input(">> ")
		
		try:
			assert len(inp_letter) == 1
		except AssertionError:
			print('try again!')
			continue
		
		if inp_letter in stuff:
			indices = [i for i,c in enumerate(stuff) if c == inp_letter]
			for i in indices:
				display[i] = inp_letter
			
		if display.count('_') == 0:
			print("correct,",''.join(display))
			game_on = False

guess_me("The witcher")