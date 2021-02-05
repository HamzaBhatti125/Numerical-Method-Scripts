a = 0
b = 10
#values of a and b are lower and upper limit of integral
no_of_points = 5 #user defined

n = no_of_points - 1
h = (b-a)/n

x = []
fx = []
j = a

def functionX(arg): #define function here
    return 3*(arg**2)

for i in range(no_of_points):
    x.append(round(j,5))
    fx.append(round(functionX(x[i]),5))
    j = j+h

print("x is: ", x)
print("fx is: ", fx)

for i in range(1,len(fx)-1):
    if i % 2 == 1:
        fx[i] = 4*fx[i]    
    else:
        fx[i] = 2*fx[i]
print("new Fx is: ", fx)

result = round((h*sum(fx))/3,5)
print("The final result is: ", result)