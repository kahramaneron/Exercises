*** The numbers which first digit is bigger than the last one between 1000 and 10000: 
for i in range(1000,10000):
	if str(i)[0] > str(i)[3]:
		print(i)
