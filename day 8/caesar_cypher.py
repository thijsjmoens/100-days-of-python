alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create function for encryption
def encrypt(original_text, shift_amount):

	# Create an empty string for decrypted word
	decrypted_word = ""

	# Loop over every char in original text
	for letter in original_text:

		# Get index number of every character and assign to a variable
		position = alphabet.index(letter)

		# change the position in alphabet
		new_position = position + shift_amount

		# Check if new position is above 26
		new_position %= len(alphabet)

		# assign new character to empty string
		decrypted_word += alphabet[new_position]

	# Output new word to console
	print(f"Your encrypted word is: {decrypted_word}")



# Create function for decryption
def decrypt(original_text, shift_amount):

	# Create an empty string for encrypted word
	encrypted_word = ""

	# Loop over every char in original text
	for letter in original_text:

		# Get index number of every character and assign to a variable
		position = alphabet.index(letter)

		# change the position in alphabet
		new_position = position - shift_amount

		# print(new_position)

		# Check if new position is above 26
	# 	new_position %= len(alphabet)

		# assign new character to empty string
		encrypted_word += alphabet[new_position]

	# Output new word to console
	print(f"Your decrypted word is: {encrypted_word}")



# Create the start function with direction
def caesar():

	# check for direction
	if direction == "encode" :

		# Call the encrypt function
		encrypt(original_text=text, shift_amount=shift)

	elif direction == "decode" :

		# Call the decrypt function
		decrypt(original_text=text, shift_amount=shift)



caesar()





