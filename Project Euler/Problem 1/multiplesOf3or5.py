i = 0
multiplesList = []
sum = 0

while i < 1000 :
    if i%3 == 0 or i%5 == 0 :
        multiplesList.append(i)
    i = i + 1

for num in multiplesList :
    sum = sum + num
else : 
    print(sum)
