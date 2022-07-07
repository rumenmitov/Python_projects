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

def findExponents(factor_array):
    exponents = {
    "Two" : 0,
    "Three" : 0,
    "Five" : 0,
    "Seven" : 0,
    "Eleven" : 0,
    "Thirteen" : 0,
    "Seventeen" : 0,
    "Nineteen" : 0 
    }

    tempExponents = {
        "Two" : 0,
        "Three" : 0,
        "Five" : 0,
        "Seven" : 0,
        "Eleven" : 0,
        "Thirteen" : 0,
        "Seventeen" : 0,
        "Nineteen" : 0
    }

    for x in factor_array:
        for y in x:
            if y == 2:
                tempExponents["Two"] += 1
            elif y == 3:
                tempExponents["Three"] += 1
            elif y == 5:
                tempExponents["Five"] += 1
            elif y == 7:
                tempExponents["Seven"] += 1
            elif y == 11:
                tempExponents["Eleven"] += 1
            elif y == 13:
                tempExponents["Thirteen"] += 1
            elif y == 17:
                tempExponents["Seventeen"] += 1
            elif y == 19:
                tempExponents["Nineteen"] += 1
            else:
                continue
        
        if tempExponents["Two"] > exponents["Two"]:
            exponents["Two"] = tempExponents["Two"]
        tempExponents["Two"] = 0

        if tempExponents["Three"] > exponents["Three"]:
            exponents["Three"] = tempExponents["Three"]
        tempExponents["Three"] = 0

        if tempExponents["Five"] > exponents["Five"]:
            exponents["Five"] = tempExponents["Five"]
        tempExponents["Five"] = 0

        if tempExponents["Seven"] > exponents["Seven"]:
            exponents["Seven"] = tempExponents["Seven"]
        tempExponents["Seven"] = 0

        if tempExponents["Eleven"] > exponents["Eleven"]:
            exponents["Eleven"] = tempExponents["Eleven"]
        tempExponents["Eleven"] = 0

        if tempExponents["Thirteen"] > exponents["Thirteen"]:
            exponents["Thirteen"] = tempExponents["Thirteen"]
        tempExponents["Thirteen"] = 0

        if tempExponents["Seventeen"] > exponents["Seventeen"]:
            exponents["Seventeen"] = tempExponents["Seventeen"]
        tempExponents["Seventeen"] = 0

        if tempExponents["Nineteen"] > exponents["Nineteen"]:
            exponents["Nineteen"] = tempExponents["Nineteen"]
        tempExponents["Nineteen"] = 0
        
        print(exponents)

    return exponents


def findAllFactors(num):
    AllFactors = []
    for x in range(1, 21):
        y = findFactors(x)
        AllFactors.append(y)
    print(AllFactors)
    return AllFactors

def findLCM(num):
    factors = findAllFactors(num)
    exponents = findExponents(factors)
    LCM = 2**exponents["Two"] * 3**exponents["Three"] * 5**exponents["Five"] * 7**exponents["Seven"] * 11**exponents["Eleven"] * 13**exponents["Thirteen"] * 17**exponents["Seventeen"] * 19**exponents["Nineteen"]
    return LCM

ans = findLCM(20)
print(ans)




        