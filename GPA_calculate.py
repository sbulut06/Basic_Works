Note1 = float(input("First exam: "))
Note2 = float(input("Second exam: "))
Final = (Note1+Note2)/2

print("Your Final Note Is: {} " .format(Final))

if Final >= 84:
    print("AA")
elif Final >= 77:
    print("AB")
elif Final >= 71:
    print("BA")
elif Final >= 66:
    print("BB")
elif Final >= 61:
    print("BC")
elif Final >= 56:
    print("CB")
elif Final >= 50:
    print("CC")
elif Final >= 46:
    print("CD")
elif Final >= 40:
    print("DC")
elif Final >= 33:
    print("DD")
else:
    print("FF")
