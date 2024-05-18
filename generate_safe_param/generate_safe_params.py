import random
from Crypto.Util.number import inverse
import sympy


def generate_safe_params(bit_length):
    p = sympy.randprime(2 ** (bit_length // 2 - 1), 2 ** (bit_length // 2))
    q = sympy.randprime(2 ** (bit_length // 2 - 1), 2 ** (bit_length // 2))

    n = p * q

    phi_n = (p - 1) * (q - 1)
    e = 65537

    d = inverse(e, phi_n)
    return n, e, d

