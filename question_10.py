
list = []
count = 0

for i in range (10000,100000):
    if str(i)[0:2] == str(i)[3:5]:
        list.append(i)
        count += 1

print(list)
print(f'Total Number is: {count}')
