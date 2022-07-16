for a in range(1, 500):
    b = (1000000 - 2000*a)/(2000 - 2*a)
    b_string = str(b)
    b_length = len(b_string)
    if b_length == 5:
        check_b = b_string[4]
        if check_b == "0":
            c = 1000 - b - a
            print("Success! The answer is:")
            print(a*b*c)
            break