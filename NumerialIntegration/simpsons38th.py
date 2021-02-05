a = 0
b = 6
#values of a and b are lower and upper limit of integral
no_of_points = 7 #user defined

n = no_of_points - 1
h = (b-a)/n

x = []
fx = []
j = a

def functionX(x): #define function here
    return 1/(1+(x**2))

for i in range(no_of_points):
    x.append(round(j,5))
    fx.append(round(functionX(x[i]),5))
    j = j+h

print("x is: ", x)
print("fx is: ", fx)

for i in range(1,len(fx)-1):
    if i % 3 == 0:
        fx[i] = 2*fx[i]    
    else:
        fx[i] = 3*fx[i]
print("new Fx is: ", fx)

result = round((3*h*sum(fx))/8,5)
print("The final result is: ", result)