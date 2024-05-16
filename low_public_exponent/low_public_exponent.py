import os
import struct
from Crypto.PublicKey import RSA
from sympy import mod_inverse, root
import gmpy2


def low_public_exponent():
    directory = "text_dir"
    c_values, n_values, public_keys = read_files(directory)

    x = chinese_remainder_theorem(c_values, n_values)
    print("Restored x:", x)

    m = calculate_m(x, public_keys[0].e)
    print("Calculated m:", m)


def read_files(directory):
    c_values = []
    n_values = []
    public_keys = []
    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'rb') as f:
                original_size = struct.unpack('<Q', f.read(8))[0]
                iv = f.read(16)
                encrypted_aes_key = f.read(256)
                c_values.append(int.from_bytes(encrypted_aes_key, byteorder='big'))

                public_key_filename = os.path.join(directory, f"public_key{i}.pem")
                with open(public_key_filename, 'rb') as key_file:
                    public_key = RSA.import_key(key_file.read())
                    n_values.append(public_key.n)
                    public_keys.append(public_key)
            i += 1

    return c_values, n_values, public_keys


def chinese_remainder_theorem(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m

    x = 0
    for i in range(len(remainders)):
        Mi = M // moduli[i]
        Mi_inverse = mod_inverse(Mi, moduli[i])
        x += remainders[i] * Mi * Mi_inverse

    return x % M


def calculate_m(x, e):
    m = root(x, e)
    integer_m = int(m.as_integer_ratio()[0])
    #TODO: make normal sqrt
    return m

