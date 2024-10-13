def calculate_love_score(name1, name2):

	# create variables
	true = 0
	love  = 0

	# Check for the letters in name1
	for letter in name1.upper():
		
		# check for letters in TRUE
		if letter == "T" or letter == "R" or letter == "U" or letter == "E":
			true += 1


		# check for letters in LOVE
		if letter == "L" or letter == "O" or letter == "V" or letter == "E":
			love += 1

	# Check for the letters in name2
	for letter in name2.upper():
		
		# check for letters in TRUE
		if letter == "T" or letter == "R" or letter == "U" or letter == "E":
			true += 1


		# check for letters in LOVE
		if letter == "L" or letter == "O" or letter == "V" or letter == "E":
			love += 1

	# Combine output
	love_signal = str(true) + "" + str(love)

	print(love_signal)



calculate_love_score("True", "Love")