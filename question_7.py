
First_digit + Second_digit is equal to Last_digit

count = 0

for i in range (100,1000):
    if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]):
        print(i)
        
print(f"{count} total numbers.")

    
