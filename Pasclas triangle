n = int(input())

a = [ [] for i in range (n)]

for i in range(n):

	for j in range (i+1):		if (j<i):

			if j == 0 :

				a[i].append(1)

			else :

				a[i].append(a[i-1][j]+a[i-1][j-1])

		elif (j==i):

			a[i].append(1)

for i in range(n):

	for j in range (n-i-1):

		print(' ' , end ='')

	for j in range (i+1):

		print(a[i][j] , end = ' ')

	print('')

		
