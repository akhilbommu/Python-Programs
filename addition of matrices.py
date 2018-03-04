m = int(input("Enter no. of rows : "))
n = int(input("Enter no. of columns : "))
Mat1 = []
for i in range(0,m):
    Mat1.append([])

for i in range(0,m):
    for j in range(0,n):
        Mat1[i].append(j)
        Mat1[i][j] = 0
print('Enter elements for first matrix')
for i in range(0,m):
    for j in range(0,n):
        print('Entry in row',i+1,'column',j+1)
        Mat1[i][j] = int(input())
print('Matrix1')
print(Mat1)
for i in range(0,m):
    for j in range(0,n):
        print(Mat1[i][j],end="      ")
    print("\n")

Mat2 = []
for i in range(0,m):
    Mat2.append([])

for i in range(0,m):
    for j in range(0,n):
        Mat2[i].append(j)
        Mat2[i][j] = 0

print("Elements for second matrix")
for i in range(0,m):
    for j in range(0,n):
        print('Entry in row',i+1,'column',j+1)
        Mat2[i][j] = int(input())
print('Matrix2')
print(Mat2)

for i in range(0,m):
    for j in range(0,n):
        print(Mat2[i][j],end="      ")
    print("\n")

Mat3 = []
for i in range(0,m):
    Mat3.append([])

for i in range(0,m):
    for j in range(0,n):
        Mat3[i].append(j)
        Mat3[i][j] = 0

for i in range(0,m):
    for j in range(0,n):
        Mat3[i][j] = Mat1[i][j] + Mat2[i][j]
print("Matrix3")
print(Mat3)

for i in range(0,m):
    for j in range(0,n):
        print(Mat3[i][j],end="      ")
    print("\n")