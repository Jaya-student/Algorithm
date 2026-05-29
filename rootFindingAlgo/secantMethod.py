def secant(f, x0, x1, eps, itmax):
    itnum = 1                           

    while True:
        x2 = x1 - (f(x1) *(x1-x0))/(f(x1)-f(x0))   

        if abs(x2 - x1) <= eps:         
            return x2, 0

        if itnum == itmax:              
            return x2, 1
        itnum += 1                      
        x0 = x1
        x1=x2                         

f  = lambda x: x**6-x- 1

root, ier = secant(f,x0=1,x1=2.0,eps=1e-7, itmax=100)

if ier == 0:
    f_root=f(root)
    print(f"Converged! Root = {root},{f_root}")
elif ier == 1:
    print(f"Max iterations reached. Best estimate = {root}")