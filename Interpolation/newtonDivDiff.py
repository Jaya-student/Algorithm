def divdif(f_values, x):
    d = f_values
    n = len(x) - 1
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            d[j] = (d[j] - d[j-1]) / (x[j] - x[j-i])
    return d

def interp(d, x, t):
    n = len(d) - 1
    p = d[n]
    for i in range(n - 1, -1, -1):
        p = d[i] + (t - x[i]) * p
    return p

x = [0, 1, 2, 3]
f = [1, 2, 5, 10]

d = divdif(f, x)
t = 1.5
print(interp(d, x, t))  