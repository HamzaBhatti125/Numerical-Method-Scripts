x = [1, 2, 3, 4, 5]
y = [5, 12, 26, 60, 97]
n = len(x) 
x2 = []
x3 = []
x4 = []
xy = []
x2y = []
for i in range(n):
    x2.append(x[i]**2)
    x3.append(x[i]**3)
    x4.append(x[i]**4)
    xy.append(x[i] * y[i])
    x2y.append((x[i]**2) * y[i])

# sumOfx = sum(x)
# sumOfy = sum(y)
# sumOfx2 = sum(x2)
# sumOfx3 = sum(x3)
# sumOfx4 = sum(x4)
# sumOfxy = sum(xy)
# sumOfx2y = sum(x2y)
print(x , "\n")
print(y , "\n")
print(x2 , "\n")
print(x3 , "\n")
print(x4 , "\n")
print(xy , "\n")
print(x2y , "\n")
print("X = ",sum(x), "\n")
print("Y = ",sum(y), "\n")
print("X2 = ",sum(x2), "\n")
print("X3 = ",sum(x3), "\n")
print("X4 = ",sum(x4), "\n")
print("XY = ",sum(xy), "\n")
print("X2Y = ",sum(x2y), "\n")