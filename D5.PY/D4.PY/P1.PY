#TAKE POSITIVE INTEGER INPUT AND TELL IF IT IS DIVISIBLE BT 5 OR 3 BUT NOT DIVISIBLE BY 15.
num = int(input("enter the positive integer:"))
if num % 15 ==0:
    print("number is divisible by 15")
else:
    if num % 3==0 or num %5==0:
        print("number is divisible by 3 or 5")
    else:
        print("number is not divisible by 3 and 5 neither by 15 ")