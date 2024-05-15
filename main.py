import random

from common_modulus import common_modulus
from wiener import wiener
from tools import generate_rsa_keys, vuln_keys

def main():
    print("\n1.The case of general module")
    print("2.Wiener's attack")
    #choice = input("Select an option:")
    choice = "2"
    if choice == "1":
        n, e1, d1, e2, d2 = generate_rsa_keys()
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
    else:
        print("Wrong_option")

if __name__ == "__main__":
    main()
