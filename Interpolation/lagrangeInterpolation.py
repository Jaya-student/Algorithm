def l(i, x, t):
    ans = 1
    for j in range(len(x)):
        if i != j:                          
            ans *= (t - x[j]) / (x[i] - x[j])
    return ans

def lagrange(y, x, t):
    s = 0
    for i in range(len(y)):
        s += y[i] * l(i, x, t)
    return s

y = [3, 12, 15]
x = [1, 2, 5]
print(lagrange(y, x, 4))  