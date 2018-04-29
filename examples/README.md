## Overview 
This is a very simple, but functional appliction of PHE (partial homomorphic encryption). Basically, you are provided with a simple form where you input senstive information (data that you don't want anyone else to be aware of). This data is encrypted on client side and then send to server for processing. 

The server in will then take the input data (cipher text or encrypted data) and perform some "useful computation" on them. In this case, the input values are multiplied by a random digit to simulate a useful computation on the encrypted data on the server side. The results are then send back to the client. At not point, data was decrypted on the server, 
so client privacy was retained throughtout the transaction. 

In more practical use cases, you can think about server as a cloud computing platfrom doing some more advance operations on client data. 

[<img src="https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png">](https://github.com/razi-rais/homomorphic-encryption/blob/master/examples/images/sample-app-img1.png)


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
