def getGCF(num1, num2):
    num1=abs(num1)
    num2=abs(num2)

    if (num1 < num2):
        helper=num1
        num1=num2
        num2=helper

    if num2 > 1:
        remainder= num1%num2
        
        if remainder == 0:
            return num2
        
        num1=num2
        num2=remainder

        return getGCF(num1, num2)
    elif num2 == 1:
        return num2
    else:
        return 1
