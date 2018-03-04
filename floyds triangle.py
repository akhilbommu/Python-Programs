n = int(input("Enter value of n : "))
a = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(a , end=" ")
        a = a + 1
        j = j + 1
    print("\n")
    i = i + 1               