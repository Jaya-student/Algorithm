def l(i, x, t):
    ans = 1
    for j in range(len(x)):
        if i != j:                          
            ans *= (t - x[j]) / (x[i] - x[j])
    return ans
def l1(i,x,t):
    deno=1
    for j in range(len(x)):
        if i!=j:
            deno *= (x[i] - x[j])
    num=0
    for k in range(len(x)):
        if k != i:
            ans=1
            for j in range(len(x)):
                if j!=i and j!=k:
                    ans*=t-x[j]
            num+=ans
    f=num/deno
    return f

        
def hermite(y1,y,x,t):
    s=0
    for i in range(len(x)):
        hi=(1-2*(l1(i,x,x[i]))*(t-x[i]))*((l(i,x,t))**2)
        hi1=(t-x[i])*((l(i,x,t))**2)
        s+=((y[i])*hi + (y1[i])*hi1)
    return s
x=[0,1,2,3]
y=[0,1,0,0]
y1=[0,0,0,0]
print(hermite(y1,y,x,2.5))