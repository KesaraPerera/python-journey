totmarks = 0

name = str(input("Enter your name: "))

mark1 = int(input("Enter your mark 01: "))
mark2 = int(input("Enter your mark 02: "))
mark3 = int(input("Enter your mark 3: "))

totmarks =(mark1 + mark2 + mark3)/3

if(totmarks >= 75):
    Grade="Your Grade is A"
elif(60<=totmarks<75):
    Grade="Your Grade is B"
elif(45<+totmarks<60):
    Grade="Your Grade is C"
elif(30<=totmarks<45):
    Grade="your Grade is D"
else:
    Grade="your Grade is F"
print("\n")
print("-----Mark Sheet------")
print("Name: ",name)
print("Grade: ",Grade)
print("Subject 01: ",mark1)
print("Subject 02: ",mark2)
print("Subject 03: ",mark3)