Heigh = float(input("Your Weight: "))
Weight = float(input("Your Height: "))
Result = Heigh / (Weight/100)**2

print("Your BMI: {}".format(round(Result)))
print("Your BMI Categories: ")


if Result <= 18.5:
    print("Underweight")
elif Result <= 24.9:
    print("Normal weight")
elif Result <= 29.9:
    print("Overweight")
elif Result <= 39.9:
    print(" low-risk Obesity")
elif Result <= 34.9:
    print("Obese (Class 1)")
elif Result <= 39.9:
    print("Obese (Class 2)")   
else:
    print("Obese (Class 3)")
