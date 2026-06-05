x=[1,3,6,8]
t=4
def y(x):
    y=[]
    for i in x:
        f=1/(1+(i*i))
        y.append(f)
    
    return y

y=y(x)
def s_i(x,k):
    i=x[k]
    f=-(2*i)/((1+i*i)**2)
    return f

def find_interval(x, t):
    for k in range(len(x) - 1):
        if x[k] <= t <= x[k+1]:
            return k
    return -1

k=find_interval(x,t)

def P(x,y,s_i,t,k):
    c1=y[k]
    c2=s_i(x,k)
    f_xi_xi1 = (y[k]-y[k+1])/(x[k]-x[k+1])
    del_xi=x[k+1]-x[k]
    c4 = (c2 + s_i(x, k+1) - 2 * f_xi_xi1) / (del_xi * del_xi)
    c3 = ((f_xi_xi1 - c2) / del_xi) - (c4 * del_xi)
    dx = t - x[k]
    p = c1 + c2 * dx + c3 * (dx ** 2) + c4 * (dx ** 3)
    return p

ans=P(x,y,s_i,t,k)
print(ans)



