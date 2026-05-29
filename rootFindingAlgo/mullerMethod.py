import numpy as np

def mullers_method(f, x0, x1, x2, tol=1e-10, max_iter=100):
    
    
    for i in range(max_iter):
        
        f0, f1, f2 = f(x0), f(x1), f(x2)
        
        
        f_x1_x0   = (f1 - f0) / (x1 - x0)          # f[x1, x0]
        f_x2_x1   = (f2 - f1) / (x2 - x1)          # f[x2, x1]
        f_x2_x1_x0 = (f_x2_x1 - f_x1_x0) / (x2 - x0)  # f[x2, x1, x0]
        
       
        w = f_x2_x1 + f_x2_x1_x0 * (x2 - x1)
        discriminant = w**2 - 4 * f2 * f_x2_x1_x0
        sqrt_disc = np.sqrt(complex(discriminant))
        if abs(w + sqrt_disc) > abs(w - sqrt_disc):
            denominator = w + sqrt_disc
        else:
            denominator = w - sqrt_disc
        
       
        dx = -2 * f2 / denominator
        x3 = x2 + dx
        
        
       
        if abs(dx) < tol:
            print(f"\n Converged in {i+1} iterations!")
            return x3
        
        
        x0, x1, x2 = x1, x2, x3
    
    print("Did not converge.")
    return x3
f = lambda x: x**3 - x - 2

root = mullers_method(f, x0=0, x1=1, x2=2)
print(f"Root found: {root}")