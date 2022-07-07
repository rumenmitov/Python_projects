from functionGCF import *

def getProduct(num1, num2):
    return num1*num2

print("\n")
print("--------------------------------")
print("* Find the LCM of two integers *")
print("--------------------------------")
print("\n")
num1=int(input("Enter number: "))
num2=int(input("Enter second number: "))

answer=str(abs(getProduct(num1, num2)) / getGCF(num1, num2))

print("The LCM is " + answer)
