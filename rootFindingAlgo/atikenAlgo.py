import numpy as np

def aitken(g, x0, eps=1e-10, max_iter=100):
    
    print(f"{'Iter':>4} | {'x2_hat':>15} | {'Error':>12}")
    print("-" * 40)
    
    for i in range(1, max_iter + 1):
        
        x1 = g(x0)                        
        x2 = g(x1)                        
        
        denom = (x2 - x1) - (x1 - x0)    
        
        if abs(denom) < 1e-15:
            print("Converged (denom≈0)")
            return x0
        
        x2_hat = x2 - (x2 - x1)**2 / denom   
        
        err = abs(x2_hat - x2)                
        print(f"{i:>4} | {x2_hat:>15.10f} | {err:>12.2e}")
        
        if err <= eps:                        
            print(f"\nRoot = {x2_hat:.10f}")
            return x2_hat
        
        x0 = x2_hat                          
    
    return x2_hat




g    = lambda x: (x + 1) ** (1/3)
root = aitken(g, x0=1.5)