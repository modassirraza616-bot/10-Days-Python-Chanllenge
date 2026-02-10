#IF COST PRICE AND SELLING PRICE OF AN ITEM IS INPUT THROUGH THE KEYBOARD, WRITE A PROGRAM TO DETERMINE WHETHER THE SELLER HAS MADE PROFIT OR INCURRED LOSS OR NO PROFIT NO LOSS. ALSO DETERMINE HOW MUCH PROFIT HE MADE OR LOSS HE INCURRED.
cost_price=int (input("enter cost price:"))
selling_price=int(input("enter selling price:"))
if cost_price<selling_price:
    print("seller has made", selling_price - cost_price,"rs profit")
elif cost_price>selling_price:
    print("seller has made ",cost_price - selling_price , "rs loss")
else :
    print("no profit no loss", cost_price - selling_price)    


# we can use if  and  else  statement only one time in a program but for multiple statements we use elif 
# if and elif contain statement but else doesn't. 