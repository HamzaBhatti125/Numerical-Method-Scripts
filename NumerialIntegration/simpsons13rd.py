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

print('\n-----------SIMPSONS 1/3RD-----------')
print('------------------------------')    
print('x0\tf(x(0)')
print('------------------------------')

for i in range(no_of_points):
    x.append(round(j,5))
    fx.append(round(functionX(x[i]),5))
    j = j+h
    print('%.4f\t%.4f'% (x[i],fx[i]))
    print('------------------------------')

# print("x is: ", x)
# print("fx is: ", fx)

for i in range(1,len(fx)-1):
    if i % 2 == 1:
        fx[i] = 4*fx[i]    
    else:
        fx[i] = 2*fx[i]
print("new Fx is: ", fx)

result = round((h*sum(fx))/3,5)
print("The final result is: ", result)