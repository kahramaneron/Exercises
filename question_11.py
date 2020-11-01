
biggest = 0
for i in range (1,351):
    if 125 % i == 200 % i == 350 % i :
        leftover = 125 % i
        if leftover > biggest :
            biggest = i

print('the largest number is: ', biggest)


        
