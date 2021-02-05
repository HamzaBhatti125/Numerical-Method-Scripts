a = 0
b = 1
#values of a and b are lower and upper limit of integral
no_of_points = 11 #user defined

n = no_of_points - 1
h = (b-a)/n

x = []
fx = []
j = a

def functionX(arg): #define function here
    return 1/(1 + arg**2)

for i in range(no_of_points):
    x.append(round(j,5))
    fx.append(round(functionX(x[i]),5))
    j = j+h

print("x is: ", x)
print("fx is: ", fx)

for i in range(1,len(fx)-1):
    fx[i] = 2*fx[i]
print("new Fx is: ", fx)

result = round((h*sum(fx))/2,5)
print("The final result is: ", result)