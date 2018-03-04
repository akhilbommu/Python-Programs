m = int(input("Enter no. of rows : "))
n = int(input("Enter no. of columns : "))
Mat = []
for i in range(0,m):
    Mat.append([])

for i in range(0,m):
    for j in range(0,n):
        Mat[i].append(j)
        Mat[i][j] = 0

for i in range(0,m):
    for j in range(0,n):
        print('Entry in row',i+1,'column',j+1)
        Mat[i][j] = int(input())

print(Mat)