weight = float(input("Enter Your Weight: "))
height = float(input("Enter Your height: "))
BMI = weight/(height*height)
if (BMI <18):
    print("Your BMI Value is: ",BMI,"Underweight BMI")
elif (17<BMI<26):
    print("Your BMI Value is: ",BMI,"Normal BMI")
else:
    print("Your BMI Value is: ",BMI,"Overweight BMI")
