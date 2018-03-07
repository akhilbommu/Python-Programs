m = int(input("Enter no. of rows:"))
n = int(input("Enter no. of columns:"))
Mat1=[]
for i in range(0,m):
	Mat1.append([])

for i in range(0,m):
	for j in range(0,n):
		Mat1[i].append(j)
		Mat1[i][j]=0

for i in range(0,m):
	for j in range(0,n):
		print('Entry in row',i+1,'column',j+1)
		Mat1[i][j]=int(input())

print(Mat1)

sum=0
for i in range(0,m):
    for j in range(0,n):
        if(i==j):
            sum = sum + Mat1[i][j]

print("Sum of diagonal elements is %d"%(sum))