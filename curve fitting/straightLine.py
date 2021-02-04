x = [5, 10, 15, 20, 25]
y = [16, 19, 23, 26, 30]
n = len(x) 
x2 = []
xy = []
for i in range(n):
    x2.append(x[i]**2)
    xy.append(x[i] * y[i])

sumOfx = sum(x)
sumOfy = sum(y)
sumOfx2 = sum(x2)
sumOfxy = sum(xy)
print(x , "\n")
print(y , "\n")
print(x2 , "\n")
print(xy , "\n")
print("X = ",sum(x), "\n")
print("Y = ",sum(y), "\n")
print("X^2 = ",sum(x2), "\n")
print("XY = ",sum(xy), "\n")