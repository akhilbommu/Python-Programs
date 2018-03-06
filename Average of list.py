print("Enter size of list :")
n=int(input())
list=[]
print("Enter numbers of list")
for i in range (n):
    x=int(input(""))
    list.insert(i,x)
    i+=1
print("Entered values are ",list)
sum = 0
for i in range(n):
    sum=sum+list[i]

average=sum/n
print("Average is %d"%(average))