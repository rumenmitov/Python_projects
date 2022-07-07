count = 0
number = 3
largestPrime = 0

def isPrime(number) :
    d = 2
    while d < number :
        if number%d == 0 :
            return False
        d += 1
    else :
        return True



while count <= 9999 :
    if isPrime(number) :
        largestPrime = number
        count += 1
    number += 1 

print(largestPrime)
