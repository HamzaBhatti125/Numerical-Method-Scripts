a = [[10,-3,4], [1,-3,2], [1,-2,4]]
b = [5,0,3]


x = [0]
y = [0]
z = [0]

for i in range(11):
    x.append(((1/a[0][0])*(b[0]-(a[0][1]*y[i])-(a[0][2]*z[i]))))
    y.append(((1/a[1][1])*(b[1]-(a[1][0]*x[i])-(a[1][2]*z[i]))))
    z.append(((1/a[2][2])*(b[2]-(a[2][0]*x[i])-(a[2][1]*y[i]))))
    print('%.4f\t%.4f\t%.4f\t%0.4f'% (i,x[i],y[i],z[i]))
    print('------------------------------')

