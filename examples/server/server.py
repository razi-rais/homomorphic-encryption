from phe import paillier
import json
from random import *
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['POST'])
def process():

    if request.method == 'POST':
       
       received_dict = json.loads(request.data)
       public_key_rec = paillier.PaillierPublicKey(n=int(received_dict['public_key']['n']))
       enc_nums_rec = [paillier.EncryptedNumber(public_key_rec, int(x[0]), int(x[1])) for x in received_dict['values']]
       x = randint(1, 10) 
       result  = {}
       result['values'] = [(str(enc_num.ciphertext()), enc_num.exponent) for enc_num in [(num * x)for num in enc_nums_rec]]

       return json.dumps(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
