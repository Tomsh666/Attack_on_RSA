from Crypto.Util.number import getPrime, inverse, getRandomRange, GCD
import math


def generate_safe_params(bit_length):
    while True:
        p = getPrime(bit_length // 2)
        q = getPrime(bit_length // 2)
        while p == q:
            q = getPrime(1024)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = getRandomRange(2, phi - 1)
        while GCD(e, phi) != 1:
            e = getRandomRange(2, phi - 1)

        d = inverse(e, phi)
        if d >= (1/3) * math.sqrt(n):
            break

    return n, e, d

