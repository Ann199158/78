import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 50 * np.sin(x)

a, b = 0, 10
n = 1000
x = np.linspace(a, b, n)

y = f(x)
y_interp = np.zeros(n)
for i in range(1, n - 1):
    y_interp[i] = y[i] + (y[i + 1] - y[i - 1]) * (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1])

min = []
for i in range(1, n - 1):
    if y_interp[i] < y_interp[i - 1] and y_interp[i] < y_interp[i + 1]:
        min.append((x[i], y_interp[i]))

print("Первый локальный минимум: x = {:.3f}, f(x) = {:.3f}".format(min[0][0], min[0][1]))
print("Второй локальный минимум: x = {:.3f}, f(x) = {:.3f}".format(min[1][0], min[1][1]))

fig, ax = plt.subplots()
ax.plot(x, y, label="f(x)")
ax.scatter([min[0][0], min[1][0]], [min[0][1], min[1][1]], color="red", label="local min")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("f(x) = x^2 - 50*sin(x)")
plt.show()