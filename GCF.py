from functionGCF import *

print("\n")
print("----------------------------------")
print("* Finding the GCF of two integers *")
print("----------------------------------")
print("\n")
num1=int(input("Enter number: "))
num2=int(input("Enter second number: "))


answer=getGCF(num1, num2)
answer_str=str(answer)
print("GCF is " + answer_str)
