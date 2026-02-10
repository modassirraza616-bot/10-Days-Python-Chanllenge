#LENGTH OF THE LIST 
fruit =["mango", "apple", "cherry"] #create a list
print(fruit) # how to print a list
print(type(fruit)) # how to find the datatype of the list
print(len(fruit))  # how to find the list of the list
# checking if an item is in the list 
if "mango" in fruit:
    print("yes mango item is in a list")
else:
    print("mango is not in the list") 

# if item is not present in the list
if "guava" not in fruit:
    print("guava is not in a list")
else:
    print("guava is in the list")
