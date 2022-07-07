def isPalindrome(number) :
    listOfNumber = list(number)
    listOfNumber_length = len(listOfNumber)
    if listOfNumber_length == 6 :
        if listOfNumber[0] == listOfNumber[5] and listOfNumber[1] == listOfNumber[4] and listOfNumber[2] == listOfNumber[3] :
            return True
        else :
            return False
    else :
        if listOfNumber[0] == listOfNumber[4] and listOfNumber[1] == listOfNumber[3] :
            return True
        else :
            return False



def findPalindrome() :
    palindromes = []

    for num1 in range(999, 99, -1) :
        for num2 in range(999, 99, -1) :
            product = num1 * num2
            product_str = str(product)
            if isPalindrome(product_str) :
                print(product_str + " is a PALINDROME!!!!!")
                palindromes.append(product)
            else :
                print(product_str + " is not a palindrome")
    return palindromes
                    
palindromes = findPalindrome()
print(palindromes)
highestPalindrome = 0
for x in palindromes :
    if x > highestPalindrome :
        highestPalindrome = x
print(highestPalindrome)

