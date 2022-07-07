numbers = []
for x in range(1,101) :
    numbers.append(x)

def indiv_sqrs(numbers):
    indiv_sum = 0
    for x in numbers :
        indiv_sum = indiv_sum + (x)**2
    return indiv_sum

def sum_sqrs(numbers) :
    sum = 0
    for x in numbers :
        sum = sum + x
    return sum**2

individual = indiv_sqrs(numbers)
total = sum_sqrs(numbers)

print(total-individual)