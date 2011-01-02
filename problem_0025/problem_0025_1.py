import sys

n_1 = 1
n_2 = 1
n = 0
i = 3
while True:
	n = n_1 + n_2
	if (len(str(n)) == 1000):
		print i
		sys.exit()

	i = i + 1
	n_1 = n_2
	n_2 = n
