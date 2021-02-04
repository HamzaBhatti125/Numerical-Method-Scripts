import math

x = [1,2,3,4,5,6]
y = [151,100,61,50,20,8]
n = len(x) 
x2 = []
xy = []
logY = [] 
for i in range(n):
    x2.append(x[i]**2)
    logY.append(math.log(y[i],10))
    xy.append(x[i] * logY[i])

print(x , "\n")
print(y , "\n")
print(x2 , "\n")
print(logY , "\n")
print(xy , "\n")
print("X = ",sum(x), "\n")
print("Y = ",sum(logY), "\n")
print("X^2 = ",sum(x2), "\n")
print("XY = ",sum(xy), "\n")