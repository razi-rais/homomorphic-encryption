# Homomorphic Encryption

## Partially Homomorphic Encryption in Python | PHE Python Library
* Source: https://github.com/n1analytics/python-paillier
* Documentation: http://python-paillier.readthedocs.io/en/stable

This library requires bunch of dependencies that may be challenging to install specially if you're new to Linux. To save 
myself some time I end up packaging it as docker container image (ubuntu:16.04). That made it easy run it on MacOS, Linux 
and Windows (with nested virtualization enabled to run Linux container). Please do note that this is not an official docker image from the 
vendor and I don't claim any ownership or responsibility.

* Docker Image | PHE Python Library: https://hub.docker.com/r/rbinrais/python-paillier

**Example**

```
docker run --rm -it rbinrais/python-paillier:1.2.2 bash

xxxxxx@xxxxxxxxxxx:/

Python 3.5.2 (default, Nov 17 2016, 17:05:23)

[GCC 5.4.0 20160609] on linux

Type "help", "copyright", "credits" or "license" for more information.

from phe import paillier

public_key, private_key = paillier.generate_paillier_keypair()

secret_number_list = [12, 2.89763, -4.6e-12]

encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]

encrypted_number_list

[<phe.paillier.EncryptedNumber object at 0x7efd57c0f630>;,<phe.paillier.EncryptedNumber object at 0x7efd57c16358>;, <phe.paillier.EncryptedNumber object at 0x7efd553229b0>;]

[private_key.decrypt(x) for x in encrypted_number_list]

[12, 2.89763, -4.6e-12]

a, b, c = encrypted_number_list

a_plus_10 = a + 10

a_mins_b = a - b

b_times_4_7 = b * 4.7

c_div_33 = c / 33

a_plus_10

<phe.paillier.EncryptedNumber object at 0x7efd57c0f668>

a_mins_b

<phe.paillier.EncryptedNumber object at 0x7efd57c0f5c0>

b_times_4_7

<phe.paillier.EncryptedNumber object at 0x7efd55d03240>

c_div_33

<phe.paillier.EncryptedNumber object at 0x7efd55d03978>

private_key.decrypt(a_plus_10)

22

private_key.decrypt(a_mins_b)

9.10237

private_key.decrypt(b_times_4_7)

13.618861

private_key.decrypt(c_div_33)  

-1.393939393939394e-13
```

## Simple Encrypted Arithmetic Library – SEAL
Simple Encrypted Arithmetic Library – SEAL is an easy-to-use homomorphic encryption library, developed by researchers in the Cryptography Research Group at Microsoft Research. SEAL is written in C++11, and contains .NET wrappers for the public API.  

* Download/Documentation: https://www.microsoft.com/en-us/research/project/simple-encrypted-arithmetic-library-seal-2 

# Learning Resources 

* A brief survey of Fully Homomorphic Encryption, computing on encrypted data: https://blog.quarkslab.com/a-brief-survey-of-fully-homomorphic-encryption-computing-on-encrypted-data.html
* Fast Private Set Intersection from Homomorphic Encryption: https://eprint.iacr.org/2017/299
* Homomorphic encryption application on FinancialCloud framework: http://ieeexplore.ieee.org/document/7850013
* A protocol for verification of an auction without revealing bidvalues http://ac.els-cdn.com/S1877050910002991/1-s2.0-S1877050910002991-main.pdf?_tid=329bce50-7177-11e7-adca-00000aacb362&acdnat=1501014422_9b482e07b3f3fd2951dab8b4108109a3
* Private Queries on Encrypted Genomic Data: https://eprint.iacr.org/2017/207.pdf


