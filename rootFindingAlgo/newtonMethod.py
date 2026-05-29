def newton(f, df, x0, eps, itmax):
   
    itnum = 1                           
    while True:
        denom = df(x0)                  
        if denom == 0:                  
            return None, 2

        x1 = x0 - f(x0) / denom        

        if abs(x1 - x0) <= eps:        
            return x1, 0

        if itnum == itmax:             
            return x1, 1

        itnum += 1                     
        x0 = x1                        


f  = lambda x: x**6-x- 1
df = lambda x: 6*x**5-1

root, ier = newton(f, df, x0=2.0, eps=1e-7, itmax=100)

if ier == 0:
    print(f"Converged! Root = {root}")
elif ier == 1:
    print(f"Max iterations reached. Best estimate = {root}")
elif ier == 2:
    print("Error: derivative was zero at starting point.")