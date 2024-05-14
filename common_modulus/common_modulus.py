from Crypto.Util.number import GCD, inverse
import random


def common_modulus(n, e2, d2, e1):
    tmp = e2 * d2 - 1
    f = 0
    while tmp % 2 == 0:
        tmp //= 2
        f += 1
    s = tmp

    while True:
        a = random.randint(2, n - 1)
        b = pow(a, s, n)
        l = 1
        while pow(b, pow(2, l), n) != 1:
            l += 1
        if pow(b, pow(2, l-1), n) != b-1:
            t = pow(b, pow(2, l-1), n)
            break
    p = GCD(t + 1, n)
    q = GCD(t - 1, n)
    phi = (p - 1)*(q - 1)
    d1 = inverse(e1, phi)
    return d1, p, q

