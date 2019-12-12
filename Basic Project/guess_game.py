def main():
	print('\t\t___Sheraz Project___')
	print()

	print('Guess the Secret Number which is in b/w 1 to 9')

	#initialize veriables
	secret = 0
	guess = 0
	guess_count = 0
	turn_left = 0
	print()

#taking input form user
	while True:
		guess_limit = int(
			input('How many Turns you want. Your Turn in between 1 to 3: '))
		if guess_limit <= 3 and guess_limit > 0:
			break

	turn_left = guess_limit

#logic in between while loop
	while guess_count < guess_limit:
		print()
		guess = int(input('Guess: '))
		guess_count += 1
		turn_left -= 1
		secret += 3

		#if guess code is wrong do this
		if guess != secret:
			print(f"{guess} is not the Secret Code")
			print(f"Turn Left: {turn_left}")

			#if guess is right do this
		elif guess == secret:
			print()
			print('\t___You Win___')
			print(f'{secret} is the Secret Code')
			break

	else:
		print()
		print('\t___You Loss___')
		print(f'The Secret Code is {secret}')


main()
