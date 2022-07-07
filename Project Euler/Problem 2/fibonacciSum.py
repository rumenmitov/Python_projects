num1 = 1
num2 = 1
result = 0
sum = 0

while result < 4000000 :
    result = num1 + num2
    if result%2 == 0 :
        sum = sum + result
    
    num1 = num2
    num2 = result

print(sum)
