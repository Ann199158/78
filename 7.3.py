import numpy as np

n = 20
eps = 1e-6
max_iter = 100

x = np.ones(n) / n

def F(x):

    f = np.zeros(n)
    for i in range(n):
        for j in range(n):
            f[i] += np.cos(x[j]) + i * (1 - np.cos(x[i])) - np.sin(x[i])
        f[i] = n - f[i]
    return f

def J(x):

    jac = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                jac[i, j] = 1j * np.sin(x[i]) - i * n * np.sin(x[i])
            else:
                jac[i, j] = -1j * np.sin(x[i])
    return jac



for i in range(max_iter):
    f = F(x)
    if np.linalg.norm(f) < eps:
        break

    Jx = J(x)
    dx = np.linalg.solve(Jx, -f)
    x += dx.real

print("Решение системы уравнений:")
print(x)