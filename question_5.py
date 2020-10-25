*** The palindromic numbers between 1000 and 10000:
    for i in range(1000,10000):
	if str(i)[0]==str(i)[3] and str(i)[1]==str(i)[2]:
		print(i)
