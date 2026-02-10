n = int(input ("enter n:"))
for i in range (1,n+1):  #loop for rows
    for j in range(1,i):  # loop for columns
        print(j, end="")
    print(i)     