# Numerical Methods in Python

A Python implementation of classical numerical analysis algorithms — covering **root-finding methods** and **interpolation techniques** — with a focus on mathematical rigour, convergence analysis, and visualization.

---

## Overview

Numerical methods are the backbone of scientific computing. When equations cannot be solved analytically, we rely on iterative algorithms that converge to solutions with guaranteed precision. This repository implements and compares several such algorithms from scratch, exploring their convergence properties and computational trade-offs.

---

## Algorithms Implemented

### Root Finding (`/rootFindingAlgo`)

Root-finding algorithms solve for $x$ such that $f(x) = 0$.

| Method | Convergence | Key Idea |
|---|---|---|
| **Bisection Method** | Linear — $O(1/2^n)$ | Repeatedly halves the interval containing the root |
| **Newton-Raphson** | Quadratic — $O(e^2)$ | Uses tangent line approximation via $f'(x)$ |
| **Secant Method** | Superlinear — $O(e^{1.618})$ | Finite difference approximation of the derivative |

**Why it matters:** Root-finding underlies optimization solvers, physics simulations, financial models (e.g. implied volatility), and machine learning loss minimization.

### Interpolation (`/Interpolation`)

Interpolation reconstructs an unknown function from a discrete set of data points.

| Method | Description |
|---|---|
| **Lagrange Interpolation** | Constructs a unique polynomial passing through all given points |
| **Newton's Divided Differences** | Efficient recursive formulation of the interpolating polynomial |

**Why it matters:** Interpolation is fundamental in signal processing, computer graphics, numerical integration (quadrature), and solving differential equations.

---

## Mathematical Background

### Newton-Raphson Method

Given $f: \mathbb{R} \to \mathbb{R}$, starting from an initial guess $x_0$:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

This arises from a first-order Taylor expansion of $f$ around $x_n$. Under mild smoothness conditions ($f''$ exists and is bounded near the root), convergence is **quadratic** — the number of correct digits roughly doubles each iteration.

### Lagrange Interpolating Polynomial

Given $n+1$ data points $(x_0, y_0), \ldots, (x_n, y_n)$:

$$P(x) = \sum_{j=0}^{n} y_j \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{x - x_k}{x_j - x_k}$$

A key concern is **Runge's phenomenon** — high-degree polynomial interpolation on equally spaced points can diverge wildly at the edges. Chebyshev nodes are often preferred to mitigate this.

---

## Newton Fractals (Bonus)

The file `newtonFractal.py` extends Newton-Raphson to the **complex plane**, revealing the fractal basin boundaries that emerge when solving polynomial equations like $z^3 - 1 = 0$.

Each pixel in the output image represents a complex starting point $z_0$; its color indicates which root Newton's method converges to from that starting point. The intricate boundary between basins is a **Julia set** — a fractal of infinite complexity arising from a simple iterative rule.

> This connects classical numerical analysis to complex dynamics, a rich area of modern mathematics.

---

## Requirements

```bash
pip install numpy matplotlib
```

---

## Usage

```bash
# Run a root-finding example
python rootFindingAlgo/newton.py

# Run interpolation
python Interpolation/lagrange.py

# Generate Newton fractal
python newtonFractal.py
```

---

## Repository Structure

```
Algorithm/
├── rootFindingAlgo/       # Bisection, Newton-Raphson, Secant, Fixed-point
├── Interpolation/         # Lagrange, Newton's divided differences
├── newtonFractal.py       # Complex Newton's method + fractal visualization
└── README.md
```

---

## References

- Burden & Faires, *Numerical Analysis* (10th ed.)
- Trefethen, *Approximation Theory and Approximation Practice*
- Devaney, *An Introduction to Chaotic Dynamical Systems*

---

*Implemented as part of coursework in Numerical Methods — Mathematics & Computing, IIT Delhi.*
