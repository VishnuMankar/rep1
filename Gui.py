picture  =  [

  [0,0,0,1,0,0,0],

  [0,0,1,1,1,0,0],

  [0,1,1,1,1,1,0],

  [1,1,1,1,1,1,1],

  [0,0,0,1,0,0,0],

  [0,0,0,1,0,0,0]

  ]

   

for i in picture:

	for pixel in i:		if (pixel == 1):

			print('*', end='')

		else:

			print(' ', end='')

	print('')

	
