list=[]
print("Enter size of list :")
n=int(input())
list=[]
print("Enter numbers of list")
for i in range (n):
    x=int(input(""))
    list.insert(i,x)
    i+=1
print("Entered values are ",list)
print("Enter element to be searched :")
element=int(input())
for i in range(n):
    if(list[i]==element):
        print