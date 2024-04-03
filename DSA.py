
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
    k = random.randint(1, q-1)
    print(k)
    r = ((g**private_key) % p) % q
    print(r)
    s = ((1/k)*(hash(message)+private_key*r)) % q
    print(s)
    return (r, s)


def verify(signature, tampered_message, p, q, g, public_key) -> bool:
    r, s = signature
    w = (1/s) % q
    print(w)
    u1 = (hash(tampered_message)*w) % q
    print(u1)
    u2 = (r*w) % q
    print(u2)
    v = (((g**u1)*(public_key**u2)) % p) % q
    print(v)
    return r == v


def main():
    p = 11
    q = 5
    h = 8
    g = h**((p-1)/q) % p
    msg = "Salam"
    x = random.randint(1, q-1)
    y = (g**x) % p

    print(p)
    print(q)
    print(g)
    print(x)
    print(y)
    signature = sign(msg, p, q, g, x)
    result = verify(signature, msg, p, q, g, y)
    print("result({result}})".format(True, False))


main()
