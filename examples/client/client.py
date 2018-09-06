from phe import paillier
import json
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import send_from_directory
from flask_cors import CORS
import requests

app = FlaskAPI(__name__)
cors = CORS(app, resources={r'/*': {"origins": '*'}})

public_key, private_key = paillier.generate_paillier_keypair()

def encrypt(input):

    encrypted_number_list = [public_key.encrypt(x) for x in input]
    enc_with_one_pub_key = {}
    enc_with_one_pub_key['public_key'] = {'g': public_key.g, 'n': public_key.n}
    enc_with_one_pub_key['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_number_list]
    json_content = json.dumps(enc_with_one_pub_key)

    return json_content

def serialize(data):

    json_content = json.dumps(data)
    return json_content

@app.route("/", methods=['GET','POST'])
def process():

  if (request.method == 'POST'):

    
    data = request.json
    if data: 

        print ("Input Data: ", data)

        numbers = [int(e) for e in data['input'].split(',')]
        json_content = encrypt(numbers)
        result = requests.post(data['dns'],json=json_content)
        data = json.loads(result.text)

        #decryption
        enc_nums  = [paillier.EncryptedNumber(public_key, int(x[0]), int(x[1])) for x in data['values']]
        plain_nums = {}
        plain_nums['output'] = [private_key.decrypt(x) for x in enc_nums]
        results = json.dumps(plain_nums)
        return results

@app.route("/css/<path:filename>")
def send_file(filename):  
    return send_from_directory('css', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

