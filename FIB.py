"""

Problem: Rabbits and Recurrence Relations
ID: FIB
URL: http://rosalind.info/problems/fib/
Solution author: Samael Olascoaga

"""

def fibo(n, k):
	if n == 1:
		return 1
	elif n == 2:
		return k
	else:
		one_gen = fibo(n - 1, k)
		second_gen = fibo(n - 2, k)
	if n <= 4:
		return(one_gen + second_gen)

	return (one_gen + (second_gen * k))
