import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = float(real)
        self.imag = float(imag)
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError()
        r = (self.real * other.real + self.imag * other.imag) / denom
        i = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(r, i)
    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

def complex_pow(z, power):
    if power == 0:
        return Complex(1.0, 0.0)
    result = z
    for _ in range(1, power):
        result = result * z
    return result

def newton(f, df, x0, eps=1e-10, itmax=60):
    for step in range(itmax):
        fx  = f(x0)
        dfx = df(x0)
        if abs(dfx) == 0:
            return None, itmax
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < eps:
            return x1, step
        x0 = x1
    return x0, itmax
n = 8 #no. of roots
def f(z):
    return complex_pow(z, 8) - Complex(1.0, 0.0) #define f

def df(z):
    return Complex(8.0, 0.0) * complex_pow(z, 7)#define df

np_roots = np.roots([1, 0, 0, 0, 0, 0, 0, 0, -1])
roots = [Complex(r.real, r.imag) for r in np_roots]

def get_root_index(root, tol=1e-2):
    if root is None:
        return -1
    for i, r in enumerate(roots):
        if abs(root - r) < tol:
            return i
    return -1

def compute_fractal(xmin, xmax, ymin, ymax, width, height, itmax):
    root_grid  = np.zeros((height, width), dtype=int)
    steps_grid = np.zeros((height, width), dtype=float)
    for row in range(height):
        for col in range(width):
            real = xmin + (xmax - xmin) * col / width
            imag = ymin + (ymax - ymin) * row / height
            z0 = Complex(real, imag)
            root, steps = newton(f, df, z0, itmax=itmax)
            idx = get_root_index(root)
            root_grid[row, col] = idx
            steps_grid[row, col] = steps
    return root_grid, steps_grid

ITMAX = 50
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
root_grid, steps_grid = compute_fractal(xmin, xmax, ymin, ymax, width=800, height=800, itmax=ITMAX)

rootColors = cm.rainbow(np.linspace(0, 1, n))[:, :3]
height, width = root_grid.shape
img = np.zeros((height, width, 3))

for row in range(height):
    for col in range(width):
        root_idx = root_grid[row, col]
        steps    = steps_grid[row, col]
        if root_idx == -1:
            img[row, col] = [0.0, 0.0, 0.0]
        else:
            base_color = rootColors[root_idx]
            norm_steps = steps / ITMAX
            grad_factor = max(0.35, 1.0 - (norm_steps ** 0.6))
            img[row, col] = base_color * grad_factor

plt.figure(figsize=(10, 10))
plt.imshow(img, extent=[xmin, xmax, ymin, ymax], origin='lower', interpolation='bilinear')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.tight_layout()
plt.show()
