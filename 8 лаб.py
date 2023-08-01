
def f(x):

     return x ** 4 -1.6 * x ** 3 - 3 * x ** 2 + 8.5 * x

def f_prime(x):
    return 4 * x ** 3 + 3 * (-1.6) * x ** 2 + 2 * (-3) * x + 8.5


def method(f, f_prime, x0, eps=1e-7, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx) < eps:
            return x
        x -= fx / fpx

    return x


x_min = method(f, f_prime, x0 = 1)

print("Минимум функции:", f(x_min))
print("x минимума:", x_min)