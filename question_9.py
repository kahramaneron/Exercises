#numbers which its first_digit + second_digit + third_digit < 9
#between 1 and 999

list = []

for i in range (1,10):
    if int(str(i)[0]) < 9:
        list.append(i)
        

for i in range (10,100):
    if int(str(i)[0]) + int(str(i)[1]) < 9:
        list.append(i)
        

for i in range (100,1000):
    if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) < 9:
        list.append(i)

print(list, sep=',')
