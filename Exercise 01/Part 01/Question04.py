#For Loop
totalMarks=0
for i in range (1,6):
    marks = int(input(f"Enter Mark {i}:"))
    totalMarks = marks+totalMarks

print("Total Marks is: ",totalMarks)