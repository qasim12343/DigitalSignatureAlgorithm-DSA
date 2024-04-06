
import math
import random


# def primeFactors(n):

#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         print(2),
#         n = n / 2

#     for i in range(3, int(math.sqrt(n))+1, 2):

#         while n % i == 0:
#             print(i),
#             n = n / i

#     if n > 2:
#         print(n)


# n = 107
# primeFactors(n)
MAX = 1000000007


def hash(message):
    res = 1
    for c in message:
        res = res * ord(c) % MAX
    return res


def sign(message, p, q, g, private_key):
    s = 0
    r = 0
    while s == 0 or r == 0:
        k = random.randint(1, q-1)
        r = int(((g**k) % p) % q)
        s = int((pow(k, -1)*(hash(message)+private_key*r)) % q)
    print("k = ", k)
    print("r = ", r)
    print("s = ", s)
    return (r, s)


def verify(signature, tampered_message, p, q, g, public_key) -> bool:
    r, s = signature
    w = pow(s, -1) % q
    print("w = ", w)
    u1 = (hash(tampered_message)*w) % q
    print("u1 = ", u1)
    u2 = (r*w) % q
    print("u2 = ", u2)
    v = ((g**u1)*(public_key**u2) % p) % q
    print("v = ", v)
    return r == v


def main():
    p = 23
    q = 11
    g = 1
    while g == 1:
        h = random.randint(2, p-2)
        g = int(pow(h, (p-1)/q) % p)

    msg = "Salam"
    x = random.randint(1, q-1)
    y = int((g**x) % p)

    print("p = ", p)
    print("q = ", q)
    print("g = ", g)
    print("x = ", x)
    print("y = ", y)
    signature = sign(msg, p, q, g, x)
    result = verify(signature, msg, p, q, g, y)
    print(f"result({result})")


main()
