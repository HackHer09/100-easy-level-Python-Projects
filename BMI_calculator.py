print("Welcome to BMI Calculator !")
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))
BMI = weight / (height**2)#This is the formula
#rounds the BMI to 2 decimal places and prints
print(f"Your BMI is : {round(BMI,2)}")

#here tells user in which ctategory they fall
if 16<BMI<17 :
    print("You are Moderateyly Thin.")
if 17<BMI<18.5 :
    print("You are Mildly Thin.")
elif 18.5<BMI<25:
    print("You are Healthy(Normal).")
elif 25<BMI<30 :
    print("You are Overweight.")
elif 30<BMI<35 :
    print("You are Obese Class I.")
elif 35<BMI<40 :
    print("You are Obese Class II.")
elif 40<BMI :
    print("You are Obese Class III.")
else :
    print("You are Severely Thin.")