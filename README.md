## Overview 
This is a very simple, but functional example of PHE (partial homomorphic encryption) to achieve higher level of Privacy. In this scenario, you participate in a healthcare research study which will perform computations on your glucose and cholesterol levels and then give you the resutls back. You like to participate, but you do have following concerns related to privacy:

* You don't want to reveal your health related information (e.g. glucose and cholesterol levels) to the research institute.
* You want assurance that research institute will not able to extrapolate any information form the data. This means that in-case your data is leaked (e.g. case of data breach etc.) to 3rd party sources, your privacy still remain largely intact. 

This is a cananocial use case where homomorphic encryption make sense. Let's start with higher level workflow and then bit more discussion on technical design of the application.

### High Level Flow
You are provided with a simple input form where you enter your glucose and cholesterol levels (for this example, you can only enter integers). Thse values are senstive, and you don't want to reveal them to anyone else. These integter values are encrypted on the client side and then send to the server (running research institute based computation logic) for processing. 

Server will take the input values (cipher text/encrypted data) and then perform some "useful computation" on them. In this case, the input values are multiplied by a random digit to simulate a useful computation on the encrypted data on server side. The results are then send back to the client. At no point, data was decrypted on the server, 
so client privacy was retained throughtout the transaction. 

In more practical use cases, you can think about server as a cloud computing platfrom doing some more advance operations on client data. 


[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png">](https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png)


## Technical

The client and server are implemented using Pyhton.

* Client UI - Application front end based on on HTML and JQuery with Python Flask API on backend. The client application simply makes a RESTful call to a client api endpoint.

* Client API: RESTful endpoint that take JSON input, and then perform homomorphic encryption operations [n1analytics/python-paillier](https://github.com/n1analytics/python-paillier) library. It then POST the cipher text in JSON format to server API endpoint.

* Server API: RESTful endpoint that takes JSON input and multiply the cipher text to a random integer (plain text).
All encryption operations use [n1analytics/python-paillier](https://github.com/n1analytics/python-paillier) library. It then send the response back in JSON format.  

#### NOTE: You can clone the code available in the ```/examples``` and then run it. I would recommend using the instructions below, to get everything up and running quickly using Docker. This also helps you avoid installing Python paillier library locally which has number of depedencies.

## Prequesites:
* Docker (NOTE: Install Docker version based on your OS. For Windows, please use Docker for Windows since this sample is leverages Linux Docker containers).

## Run
The docker-compose command will build both client and server containers if they are not already present in docker registry. 

```
docker-compose up
```
## Test

#### CURL Command 
```
curl -H "Content-Type: application/json" -X POST http://localhost:5000 -d @sample-input-for-post-request.json
```
##### Output 
Please note that actual output may vary as the server mulitples the input values with a random number. 
```
{"output": [40, 44]}
```

#### Postman

[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/postman.png">](https://https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/postman.png)


# More Resources

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


