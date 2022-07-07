a = 3
b = 4
c = 5

while c < 333 :
    a = 3
    b = 4
    while b < 332 :
        a = 3
        while a < 331 :
            if (a**2) + (b**2) == (c**2) :
                if a + b + c == 1000 :
                    print(a*b*c)
                    break
            a += 1
            print(a)
        b += 1
    c += 1