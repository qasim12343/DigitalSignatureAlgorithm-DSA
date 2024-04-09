
import random
from gmpy2 import invert, powmod


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
        k = random.randrange(2, q)
        r = int(((g**k) % p) % q)
        s = int((invert(k, q)*(hash(message)+private_key*r)) % q)
    print(k)
    print(r)
    print(s)
    return (r, s)


def verify(signature, tampered_message, p, q, g, public_key) -> bool:
    r, s = signature
    w = invert(s, q)
    print(w)
    u1 = (hash(tampered_message)*w) % q
    print(u1)
    u2 = (r*w) % q
    print(u2)
    v = int(((g**u1)*(public_key**u2) % p) % q)
    print(v)
    return r == v


def main():
    p = 23
    q = 11
    g = 1
    while g == 1:
        h = random.randint(2, p-2)
        g = int(pow(h, (p-1)/q) % p)

    SentMsg = input()
    RecievedMsg = input()
    x = random.randint(1, q-1)
    y = int(pow(g, x)) % p

    print(p)
    print(q)
    print(g)
    print(x)
    print(y)
    signature = sign(SentMsg, p, q, g, x)
    result = verify(signature, RecievedMsg, p, q, g, y)
    print(result)


main()
