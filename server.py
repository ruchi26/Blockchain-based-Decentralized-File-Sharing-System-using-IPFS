import os
import urllib.request
import ipfshttpclient
from my_constants import app
from flask import Flask, flash, request, redirect, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
from blockchain import Blockchain

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

blockchain = Blockchain()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hashed(filename):
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    hashed_file = client.add(filename)['Hash']
    return  hashed_file

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/add_file', methods=['POST'])
def add_file():
    if request.method == 'POST':
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
                file_hash = 'ABDEFgh'
            # hashed_output1 = hashed(filename)
                sender = 'Ruchika'
                receiver = 'Souvik'
                index = blockchain.add_file(sender, receiver, file_hash)
                message = f'This file will be added to Block {index}'
            else:
                message = 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'
        response = {'message': message}
        return jsonify(response),  201

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)