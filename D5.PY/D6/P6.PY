for i in range(1,4,1):
    for j in range(1,4-i):
        print(" ", end=" ")
    for k in range(1,2*i):
        print(k, end=" ")
    print()  