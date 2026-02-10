#TAKE INPUT PERCENTAGE OF A STUDENT AND PRINT THE GRADE ACCORDING TO MARKS:
n = int (input("enter the percentage:"))
if n>=81 and n<=100:
    print("very good")
elif n>=61 and n<=80:
    print("good")
elif n>41 and n<=60:
    print("average")
else:
    print("fail")        