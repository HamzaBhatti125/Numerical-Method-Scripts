x0 = 0
y0 = 1
h = 0.5
x1 = 2
# these above things are user defined

n = int((x1-x0)/h)

xn = []
yn = []
yn2 = []
func = []

def functionOFX(x,y):
    return ((y*(x**2)) - (1.1*y)) #define function here

def funcOfyn1(a,b,c):
    return a+(b*c)

print('\n-----------EULERS METHOD-----------')
print('------------------------------')    
print('x0\ty0\tf(xn,yn)\tyn')
print('------------------------------')

for i in range(n+1):
    xn.append(round(x0,3))
    yn.append(round(y0,3))
    func.append(round(functionOFX(xn[i],yn[i]),3))
    yn2.append(round(funcOfyn1(yn[i],h,functionOFX(xn[i],yn[i])),3))
    x0 += h
    y0 = yn2[i]
    print('%.4f\t%.4f\t%0.4f\t%.4f'% (xn[i],yn[i],func[i],yn2[i]))
    print('------------------------------')

# print("xn is: ",xn)
# print("yn is: ",yn)
# print("f(x,y) is: ", func)
# print("yn2 is: ",yn2)

