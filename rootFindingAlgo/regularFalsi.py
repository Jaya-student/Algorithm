def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    for i in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))   # false position formula
        fc = f(c)

        

        if abs(fc) < tol:               
            return c, i + 1

        if f(a) * fc < 0:              
            b = c
        else:                          
            a = c

    return c, max_iter
f  = lambda x: x**6-x- 1
root, iters = regula_falsi(1,2)
f_root=f(root)
print(f"\nRoot ≈ {root} found in {iters} iterations and value at it is {f_root}")