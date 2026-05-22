side_A = int(input("Enter Side A: "))
side_B = int(input("Enter Side B: "))
side_C = int(input("Enter Side C: "))
if(side_A+side_B>side_C & side_A+side_C>side_B & side_B+side_C>side_A):
    print("Valid triangle")
else:
    print("Invalid triangle")