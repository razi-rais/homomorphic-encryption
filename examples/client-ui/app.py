from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route('/')

def main():

    return render_template('home.html')

@app.route('/', methods=['POST','GET'])
def my_form_post():
    text = request.form['input_glu_level']
    processed_text = text.upper()

    return render_template('home.html')

   
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=7000)
