list=[]
print("Enter size of list :")
size=int(input())
print("Enter numbers of list")
for i in range (size):
    x=int(input(""))
    list.insert(i,x)
    i+=1
print("Entered numbers are ",list)
for i in range(size):
    for j in range(size-i-1):
        if ( list[j] > list[j+1]) :
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print("Entered numbers in ascending order are",list)