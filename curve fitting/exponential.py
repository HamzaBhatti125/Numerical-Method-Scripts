import math

x = [1,2,3,4,5,6]
y = [151,100,61,50,20,8]
n = len(x) 
x2 = []
xy = []
logY = [] 

print('\n-----------Exponential Curve-----------')
print('------------------------------')    
print('x\t\ty\t\tx2\t\tlogY\t\txy')
print('------------------------------')

for i in range(n):
    x2.append(round(x[i]**2,2))
    logY.append(round(math.log(y[i],10),2))
    xy.append(round(x[i] * logY[i],2))
    print('%.4f\t%.4f\t%0.4f\t%.4f\t%.4f'% (x[i],y[i],x2[i],logY[i],xy[i]))
    print('------------------------------')

# print(x , "\n")
# print(y , "\n")
# print(x2 , "\n")
# print(logY , "\n")
# print(xy , "\n")
print("X = ",sum(x), "\n")
print("Y = ",sum(logY), "\n")
print("X^2 = ",sum(x2), "\n")
print("XY = ",sum(xy), "\n")