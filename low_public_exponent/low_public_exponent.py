import os
import struct
from Crypto.PublicKey import RSA
from sympy.ntheory.modular import crt
from sympy import integer_nthroot


def low_public_exponent():
    directory = "text_dir"
    c_values, n_values, public_keys, iv, original_size = read_files(directory)

    x = chinese_remainder_theorem(c_values, n_values)

    m = calculate_m(x, public_keys[0].e)
    print("Calculated m:", m)

    return m, iv, original_size


def read_files(directory):
    c_values = []
    n_values = []
    public_keys = []
    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename.startswith("file"):
            with open(os.path.join(directory, filename), 'rb') as f:
                original_size = struct.unpack('<Q', f.read(8))[0]
                iv = f.read(16)
                encrypted_aes_key = f.read(96)
                c_values.append(int.from_bytes(encrypted_aes_key, byteorder='big'))
                public_key_filename = os.path.join(directory, f"public_key{i}.pem")
                with open(public_key_filename, 'rb') as key_file:
                    public_key = RSA.import_key(key_file.read())
                    n_values.append(public_key.n)
                    public_keys.append(public_key)
            i += 1

    return c_values, n_values, public_keys, iv, original_size


def chinese_remainder_theorem(remainders, moduli):
    x, y = crt(moduli, remainders)
    return int(x)


def calculate_m(x, e):
    m, exact = integer_nthroot(x, e)
    return m
