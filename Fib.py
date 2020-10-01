def fib(n1 , n2 , n):

 if n==0 or n<0:

  return

 c = n1+n2

 print(c)

 fib(n2 , c ,n-1)

a , b = 0 , 1 

n = int (input('How many no. to print : '))

fib(a,b,n-2)
