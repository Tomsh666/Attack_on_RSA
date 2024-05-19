import random

from common_modulus import common_modulus
from wiener import wiener
from low_public_exponent import low_public_exponent
from generate_safe_param import generate_safe_params
from tools import generate_rsa_keys, vuln_keys, run_rsa, decrypt_aes


def main():
    print("\n1.The case of general module")
    print("2.Wiener's attack")
    print("3.Attack on RSA with Low Public Exponent")
    print("4.Generate parameters for RSA")
    choice = input("Select an option:")
    if choice == "1":
        n, e1, d1, e2, d2 = generate_rsa_keys(665537)
        print("\nUser 1:")
        print("n =", n)
        print("e1 =", e1)
        print("d1 =", d1)

        print("\nUser 2:")
        print("n =", n)
        print("e2 =", e2)
        print("d2 =", d2)

        d, p, q = common_modulus(n, e2, d2, e1)
        if d == d1:
            print("\nd1: ", d)
            print("p = ", p)
            print("q = ", q)
        print("Done")
    elif choice == "2":
        k = random.randint(0,3)
        e, n, d = vuln_keys(k)
        print("\nUser:")
        print("n =", n)
        print("e =", e)
        print("d =", d)
        tmp_d = wiener(e, n)
        if d == tmp_d:
            print("d =", d)
        print("Done")
    elif choice == "3":
        run_rsa(4, "text_dir")
        m, iv, original_size = low_public_exponent()
        decrypt_aes(m, iv, 4, "text_dir")
        print("Done")
    elif choice == "4":
        n, e, d = generate_safe_params(1024)
        print("n =", n)
        print("e =", e)
        print("d =", d)
        print("Done")
    else:
        print("Wrong_option")


if __name__ == "__main__":
    main()
