from sympy import symbols, cos, exp, diff
import numpy as np

x = symbols('x')

fx = exp(cos(x))

h = 3.14 / 20
a = 0
b = 3.14 / 2
eps = 0.05

xi = np.arange(a, b, h)
xi_h = [i + h/2 for i in xi]
xi = np.append(xi, 2)
yi = [fx.subs(x, i).evalf() for i in xi]
yi_h = [fx.subs(x, i + h/2).evalf() for i in xi]

def l_rec():
    sum1 = 0
    for i in range(0, len(yi) - 1):
        sum1 += yi[i]
    f1x = sum1 * h

    sum2 = 0
    for i in range(0, len(yi), 2):
        sum2 += yi[i]
    f2x = sum2 * 2 * h

    d = abs(f1x - f2x) / 3

    print(f"___Метод лівих прямокутників:___\n"
          f"Значення інтегралу:\n"
          f"При h: exp(cos(x)) = {f1x.evalf()}\nПри 2h: exp(cos(x)) = {f2x.evalf()}\nПохибка d ={d.evalf()}\n")

def r_rec():
    sum1 = 0
    for i in range(1, len(yi)):
        sum1 += yi[i]
    f1x = sum1 * h

    sum2 = 0
    for i in range(1, len(yi), 2):
        sum2 += yi[i]
    f2x = sum2 * 2 * h

    d = abs(f1x - f2x) / 3
    print(f"___Метод правих прямокутників:___\n"
          f"Значення інтегралу:\n"
          f"При h: exp(cos(x)) = {f1x.evalf()}\nПри 2h: exp(cos(x)) = {f2x.evalf()}\nПохибка d = {d.evalf()}\n")

def e_rec():
    sum1 = 0
    for i in range(0, len(yi_h) - 1):
        sum1 += yi_h[i]
    f1x = sum1 * h

    sum2 = 0
    for i in range(1, len(yi_h), 2):
        sum2 += yi_h[i]
    f2x = sum2 * 2 * h

    d = abs(f1x - f2x) / 3
    print(f"___Метод середніх прямокутників:___\n"
          f"Значення інтегралу:\n"
          f"При h: exp(cos(x)) = {f1x.evalf()}\nПри 2h: exp(cos(x)) = {f2x.evalf()}\nПохибка d = {d.evalf()}\n")

def trap():
    sum1 = 0
    for i in range(1, len(yi) - 1):
        sum1 += yi[i]
    f1x = (sum1 + (yi[0] + yi[-1]) / 2) * h

    sum2 = 0
    for i in range(2, len(yi), 2):
        sum2 += yi[i]
    f2x = (sum2 + (yi[0] + yi[-1]) / 2) * 2 * h

    d = abs(f1x - f2x) / 3
    print(f"___Метод трапецій:___\n"
          f"Значення інтегралу:\n"
          f"При h: exp(cos(x)) = {f1x.evalf()}\nПри 2h: exp(cos(x)) = {f2x.evalf()}\nПохибка d = {d.evalf()}\n")

def simpson():
    v0 = yi[1] + yi[-1]

    v1 = 0
    for i in range(0, len(yi_h) - 1):
        v1 += yi_h[i]

    v2 = 0
    for i in range(0, len(yi) - 1):
        v2 += yi[i]

    v3 = 0
    for i in range(1, len(yi_h) - 1, 2):
        v3 += yi_h[i]

    v4 = 0
    for i in range(0, len(yi_h) - 1, 2):
        v3 += yi_h[i]

    f1x = (v0 + 4 * v1 + 2 * v2) * h / 6
    f2x = (v0 + 4 * v3 + 2 * v4) * h / 3

    d = abs(f1x - f2x) / 15
    print(f"___Метод криволінійних трапецій Сімпсона:___\n"
          f"Значення інтегралу:\n"
          f"При h: exp(cos(x)) = {f1x.evalf()}\nПри 2h: exp(cos(x)) = {f2x.evalf()}\nПохибка d = {d.evalf()}\n")

def simpson_e():
    m = max([diff(exp(cos(x)), x, 4).subs(x, i) for i in xi])
    n = round((((b - a) ** 5) * m) /(180 * eps))
    h1 = (b - a) / n

    xi1 = np.arange(a, b, h1)
    xi1_h = [i + h1 / 2 for i in xi1]
    xi1 = np.append(xi1, 2)

    yi1 = [exp(cos(i)).evalf() for i in xi1]
    yi1_h = [exp(cos(i)).evalf() for i in xi1_h]

    v10 = yi1[1] + yi1[-1]

    v11 = 0
    for i in range(0, len(yi1_h) - 1):
        v11 += yi1_h[i]

    v12 = 0
    for i in range(0, len(yi1) - 1):
        v12 += yi1[i]

    fx = (v10 + 4 * v11 + 2 * v12) * h1 / 6
    print(f"___Метод криволінійних трапецій Сімпсона з точністю eps = {eps}\n"
          f"Значення інтегралу:\n"
          f"exp(cos(x)) = {fx}")


def main():
    print("Комп'ютерний практикум №8 \nВаріант №11 \nВиконав студент групи ПБ-21 \nРозумняк Руслан\n")
    l_rec()
    r_rec()
    e_rec()
    trap()
    simpson()
    simpson_e()

if __name__ == "__main__":
    main()
