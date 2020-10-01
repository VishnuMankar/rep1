import random

play_game  = 'y'

while play_game == 'y':

	your_no = int(input('what is your no? '))	a = int(input('lowest range? '))

	b = int(input('highest range? '))

	print(f'I guessed a No. between {a} and {b} : ')

	tries = 1

	

	while True:

		try_n = random.randint(a,b)

		print(try_n)

		if your_no == try_n:

			break

		else:

			d = input('Is it too high(h) or too low(l) ? ')

			if d == 'l' :

				if try_n < your_no:

					a = try_n +1

			elif d == 'h':

				if try_n > your_no:

					b = try_n -1

		tries = tries +1

	print(f'I got the No. in {tries} tries')

	play_game = input('Do you want to continue Yes(y) or No(n) ')
