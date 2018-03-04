n = int(input("Enter value of n : "))
a = 0
b = 1
print(a,end=",")
print(b,end=",")
x = a + b
for i in range(1,n+1):
    print(x,end=",")
    a = b
    b = x
    x = a + b
    i = i + 1