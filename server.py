import os
import urllib.request
import ipfshttpclient
from my_constants import app
from flask import Flask, flash, request, redirect, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
from blockchain import Blockchain
import requests

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

blockchain = Blockchain()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hashed(filename):
    url = 'https://ipfs.infura.io:5001/api/v0/add'
    files = {
        'file' : (filename),
    }
    response = requests.post(url, files=files)
    p = response.json()
    print(p['Hash'])
    # client = ipfshttpclient.connect('/dns/ipfs.infura.io/tcp/5001/https')
    # result = client.add(filename)
    hashed_file = p['Hash']
    return  hashed_file

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/add_file', methods=['POST'])
def add_file():
    if request.method == 'POST':

        error_flag = True

        # check if the post request has the file part
        if 'file' not in request.files:
            message = 'No file part'
        else:
            file = request.files['file']
            if file.filename == '':
                message = 'No file selected for uploading'

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                message = 'File successfully uploaded'
                #file_hash = 'ABDEFgh'
                hashed_output1 = hashed(filename)
                sender = request.form['sender_name']
                receiver = request.form['receiver_name']
                index = blockchain.add_file(sender, receiver, hashed_output1)
                message = f'This file will be added to Block {index}'
                error_flag = False
            else:
                message = 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'

        chain = blockchain.chain
        response = {'message': message, 'blockchain': chain}

        if error_flag == True:
            return render_template('first.html', messages = response)
        else:
            return render_template('second.html',messages = response)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)