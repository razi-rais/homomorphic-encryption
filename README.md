![Demo - Improved Privacy Using Homomorphic Encryption](https://img.youtube.com/vi/bCnIoBuWfGk/maxresdefault.jpg)
[Youtube - Demo | Improved Privacy Using Homomorphic Encryption](https://www.youtube.com/watch?v=bCnIoBuWfGk)


## Overview 
This is a very simple, but functional example of PHE (partial homomorphic encryption) to achieve a higher level of privacy. 

In this scenario: You are a participant in a healthcare research study which will perform computations on your glucose and cholesterol levels and then give you the resutls back. However, you have following concerns related to privacy:

* You don't want to reveal your health related information (e.g. glucose and cholesterol levels) to the research institute.
* You want assurance that research institute will not able to extrapolate any information form the data. This means that in-case your data is leaked (e.g. case of data breach etc.) to 3rd party sources, your privacy still remains largely intact. 

This is a cananocial use-case where homomorphic encryption makes sense. Let's start with higher level workflow, and then bit more discussion on technical design of the application.

### High Level Flow
You are provided with a simple input form where you enter your glucose and cholesterol levels (for this example, you can only enter integers). These values are senstive, and you don't want to reveal them to anyone else. These integter values are encrypted on the client-side and then are sent to the server (running research institute based computation logic) for processing. 

The server will take the input values (cipher text/encrypted data) and then perform some "useful computation" on them. In this case, the input values are multiplied by a random digit to simulate a useful computation on the encrypted data on server side. The results are then sent back to the client. At no point was data was decrypted on the server, so client privacy was retained throughtout the transaction. 

In more practical use cases, you can think about the server as a cloud computing platfrom doing some more advance operations on client data. 


[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png">](https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png)


## Technical Overview

The application has following components:

* Client UI - Application front-end based on on HTML and JQuery with Python Flask API on back-end. The client application simply makes a RESTful call to a client API endpoint. The client UI runs on localhost port 7000 by default.

* Client API -  RESTful endpoint that take JSON input, and then performs homomorphic encryption operations [n1analytics/python-paillier](https://github.com/n1analytics/python-paillier) library. It will then POST the cipher text in JSON format to server API endpoint. The client api runs on localhost port 5000 by default.

* Server API -  RESTful endpoint that takes JSON input and multiplies the cipher text to a random integer (plain text).
All encryption operations use the [n1analytics/python-paillier](https://github.com/n1analytics/python-paillier) library. It then sends the response back in JSON format. The server API runs on localhost port 80 by default.

> NOTE: You can run the code available in the ```/examples``` . I would recommend using the instructions below to get everything up and running quickly using Docker. This also helps you avoid installing Python paillier library locally, which has number of depedencies.

## Prequesites:

Install [Docker](https://docs.docker.com/install) version based on your OS. For Windows, please use Docker for Windows since this sample use Linux based Docker containers.

## Run
Launch the console (Cmd.exe on Windows, Terminal on Mac OSX and Linux). Run the docker-compose command shown below. It will build both the client and server containers, if they are not already present in your local docker registry. 

```
docker-compose up
```

Looking at the console, it should show all the containers running.

[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img2.png">](https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img2.png)


## Test

You can totally bypass the client html application and use CURL or Postman to directly call client restful endpoint.

#### CURL Command 
```
curl -H "Content-Type: application/json" -X POST http://localhost:5000 -d @sample-input-for-post-request.json
```
##### Output 
Please note that the actual output may vary as the server mulitples the input values with a random number. 
```
{"output": [40, 44]}
```

#### Postman

[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/postman.png">](https://https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/postman.png)

### UI 

Browse to the URL http://localhost:7000. Make sure you enter integters (no decimals are allowed) in the input fields, and then press *'Click here to check your risk level for (Type 1 Diabetes)'* button. 

You should see the results as comma seperated values.

[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png">](https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png)

You can change the port number from 7000 to something else, by changing the value of client-ui service port in the docker-compose file.

# More Resources

## Partially Homomorphic Encryption in Python | PHE Python Library
* Source: https://github.com/n1analytics/python-paillier
* Documentation: http://python-paillier.readthedocs.io/en/stable

This library requires a bunch of dependencies that may be challenging to install, especially if you're new to Linux. To save 
myself some time, I ended up packaging it as docker container image (ubuntu:16.04). That made it easy run it on MacOS, Linux 
and Windows (with nested virtualization enabled to run Linux container). Please do note, this is not an official docker image from the 
vendor, and I don't claim any ownership or responsibility.

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

* Download/Documentation: https://www.microsoft.com/en-us/research/project/simple-encrypted-arithmetic-library/



![Conversation with Kim Laine about SEAL](https://img.youtube.com/vi/280_1798Ej4/maxresdefault.jpg)
[Conversation with Kim Laine about SEAL](https://www.youtube.com/watch?v=280_1798Ej4)


# Learning Resources 
* Homomorphic Encryption Standardization Workshop (White Papers)  : http://homomorphicencryption.org/white-papers/
* A brief survey of Fully Homomorphic Encryption, computing on encrypted data: https://blog.quarkslab.com/a-brief-survey-of-fully-homomorphic-encryption-computing-on-encrypted-data.html
* Fast Private Set Intersection from Homomorphic Encryption: https://eprint.iacr.org/2017/299
* Homomorphic encryption application on FinancialCloud framework: http://ieeexplore.ieee.org/document/7850013
* A protocol for verification of an auction without revealing bidvalues http://ac.els-cdn.com/S1877050910002991/1-s2.0-S1877050910002991-main.pdf?_tid=329bce50-7177-11e7-adca-00000aacb362&acdnat=1501014422_9b482e07b3f3fd2951dab8b4108109a3
* Private Queries on Encrypted Genomic Data: https://eprint.iacr.org/2017/207.pdf



