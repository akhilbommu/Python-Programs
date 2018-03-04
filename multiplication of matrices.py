m1 = int(input("Enter no. of rows : "))
n1 = int(input("Enter no. of columns : "))
Mat1 = []
for i in range(0,m1):
    Mat1.append([])

for i in range(0,m1):
    for j in range(0,n1):
        Mat1[i].append(j)
        Mat1[i][j] = 0

for i in range(0,m1):
    for j in range(0,n1):
        Mat1[i][j] = int(input())

print(Mat1)

m2 = int(input("Enter no. of rows : "))
n2 = int(input("Enter no. of columns : "))
Mat2 = []
for i in range(0,m2):
    Mat2.append([])

for i in range(0,m2):
    for j in range(0,n2):
        Mat2[i].append(j)
        Mat2[i][j] = 0

for i in range(0,m2):
    for j in range(0,n2):
        Mat2[i][j] = int(input())

print(Mat2)

print("Product of entered matrices\n")
Mat3 = []
for i in range(0,m1):
    Mat3.append([])

for i in range(0,m1):
    for j in range(0,n2):
        Mat3[i].append(j)
        Mat3[i][j] = 0

for i in range(0,m1):
    for j in range(0,n2):
        for k in range(0,m2):
            Mat3[i][j] = Mat3[i][j] + Mat1[i][k] * Mat2[k][j]

print(Mat3)
