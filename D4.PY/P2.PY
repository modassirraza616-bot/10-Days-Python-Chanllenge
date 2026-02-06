# MATCH CASE
'''IF THERE IS 1 VARIABLE BUT MORE NUMBER OF STATEMENT THEN USE MATCH CASE'''
#EXAMPLE
n= int (input("enter 1st number:"))
m=int(input("enter 2nd number:"))
o= input("enter operation:")
match o:
    case "+":
        print("addition:", n+m)
    case "_":
        print("subtraction:", n-m)
    case "*":
        print("multiply:",n*m)
    case "/":
        print("divide:",n/m)
    case _ :
        print("enter valid operator")            

