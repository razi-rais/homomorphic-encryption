
## Prequesites:
* Docker (NOTE: Install Docker based on your OS. For Windows, use Docker for Windows since containers Linux based).

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
