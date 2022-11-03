score = input("Enter Score: ")
sc = float(score)
if 0 <= sc <= 1:
    if sc >= 0.9:
        print("A")
    elif sc >= 0.8:
        print("B")
    elif sc >= 0.7:
        print("C")
    elif sc >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Your input value is out of range.")