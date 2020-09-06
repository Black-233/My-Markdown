list_x = [1,2,3,4,5,6,7]
list_y = [3,5,7,9,11,13,15]

#平均值计算
avx = sum(list_x)/len(list_x)
avy = sum(list_y)/len(list_y)
print('x的平均值:',avx)
print('y的平均值:',avy)

nu,nd,rd_1,rd_2 = 0,0,0,0
for num in range(0,len(list_x)):
    u = (list_x[num]-avx)*(list_y[num]-avy)
    d = (list_x[num]-avx)**2
    r_d_1 = (list_x[num]-avx)**2
    r_d_2 = (list_y[num]-avy)**2
    nu += u
    nd += d
    rd_1 += r_d_1
    rd_2 += r_d_2
b = nu/nd
a = avy - b*avx
rdo = rd_1*rd_2
r = nu/rdo**(1/2)
print('b:',b)
print('a:',a)
print('r:',r)
if a < 0:
    print('线性回归方程为:',"y = {k}x - {c}".format(k=b,c=-a))
elif a == 0:
    print('线性回归方程为:',"y = {k}x".format(k=b))
else:
    print('线性回归方程为: ',"y = {k}x + {c}".format(k=b,c=a))
