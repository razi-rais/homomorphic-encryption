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

The client and server are implemented in pyhton using Flash API. 
* Client UI - This is simple UI (based on HTML and JQuery) running on python Flask.

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
