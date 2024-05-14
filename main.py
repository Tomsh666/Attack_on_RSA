from Crypto.Util.number import getPrime, GCD, inverse
from common_modulus import common_modulus
from wiener import wiener
def generate_rsa_keys():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 665537
    while e < phi:
        if GCD(e, phi) == 1:
            break
        else:
            e += 1
    e1 = e
    d1 = inverse(e1, phi)
    e += 1
    while e < phi:
        if GCD(e, phi) == 1:
            break
        else:
            e += 1
    e2 = e
    d2 = inverse(e2, phi)
    return n, e1, d1, e2, d2

def main():
    n, e1, d1, e2, d2 = generate_rsa_keys()

    print("General module n:")
    print("n =", n)

    print("\nUser 1:")
    print("e1 =", e1)
    print("d1 =", d1)

    print("\nUser 2:")
    print("e2 =", e2)
    print("d2 =", d2)

    print("\n1.The case of general module")
    print("2.Wiener's attack")
    #choice = input("Select an option:")
    choice = "1"
    if choice == "1":
        d, p, q = common_modulus(n, e2, d2, e1)
        if d == d1:
            print("d1: ", d)
            print("p = ", p)
            print("q = ", q)
        print("Done")
    elif choice == "2":
        wiener()
    else:
        print("Wrong_option")

if __name__ == "__main__":
    main()
