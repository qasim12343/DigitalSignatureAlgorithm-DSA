# DigitalSignatureAlgorithm-DSA

![DSA](https://github.com/qasim12343/DigitalSignatureAlgorithm-DSA/assets/93463121/d0f79c5e-4234-45ba-9d37-9ad9bf3b5b91)

- p -> Prime Number 2^L-1 < p < 2^L
- q -> prime divisor of (p-1)
- g -> h^(p-1)q mod p
- h -> any Integer (1 < h < p-1)
- x -> sender private key random number between 0 and q
- y -> public key g^x mod p
- k -> any Integer (0 < k < q)

## Signature

- r = (g^x mod p) mod q
- s = [1/k(Hash(M)+x*r)] mod q

## Verifieng

- V = [(g^u1 * y^u2)mod p] mod q
- u1 = [Hash(M) w] mod q
- w = 1/s mod q
- u2 = r\*w mod q

## Comparasion

- if r == V -> True

## Inputs and Outputs

### Inputs

- Sent message
- Recieved message

### Outputs

- All variables that calculated above

## Requirment

- pip install gmpy2
