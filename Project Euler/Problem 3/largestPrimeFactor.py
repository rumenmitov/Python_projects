def findFactors(number) :
    factors = []
    d = 2
    while number > 1 :
        while number % d == 0 :
            factors.append(d)
            number /= d
        else : 
            d += 1
    else :
        return factors

factors = findFactors(600851475143)
print(factors)
highestFactor = 0

for x in factors :
    if x > highestFactor :
        highestFactor = x

print(highestFactor)




