# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilogram or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 1)} {unit}")