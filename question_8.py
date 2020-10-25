
count = 0

for i in range (100,1000,2):
    if str(i)[0] == str(i)[1]:
        count += 1 
        print(i)

    elif str(i)[0] == str(i)[2]:
        count += 1
        print(i)

    elif str(i)[1] == str(i)[2]:
        count += 1
        print(i)
        
print(f"{count} total numbers.")
    
    
