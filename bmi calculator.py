weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
height_h = height/100
bmi = weight/(height_h**2)
print("Your BMI is:",round(bmi,2))
if bmi < 18.5:
    print("category : underweight")
elif 18.5 <= bmi <2.49:
    print("category:normal weight")
elif 25 <= bmi <29.9:
    print("category:over weight gym ki vellu ra mundhu")
else:
    print("category:Obese")