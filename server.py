import os
import urllib.request
import ipfshttpclient
from my_constants import app
from flask import Flask, flash, request, redirect, render_template, url_for, jsonify
from werkzeug.utils import secure_filename
from blockchain import Blockchain
import requests

# The package requests is used in the 'hash_user_file' and 'retrieve_from hash' functions to send http post requests.
# Notice that 'requests' is different than the package 'request'.
# 'request' package is used in the 'add_file' function for multiple actions.

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

blockchain = Blockchain()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hash_user_file(file_content):
    url = 'https://ipfs.infura.io:5001/api/v0/add'
    user_file = { 'file' : (file_content), }
    response = requests.post(url, files = user_file)
    hashed_file = response.json()['Hash']
    return hashed_file

def retrieve_from_hash(file_hash):
    url = 'https://ipfs.infura.io:5001/api/v0/cat?arg=' + file_hash
    response = requests.get(url)
    file_content = (response.text).encode('utf8')
    
    file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], file_hash)
    user_file = open(file_path, 'ab')
    user_file.write(file_content)
    return file_content

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/add_file', methods=['POST'])
def add_file():
    if request.method == 'POST':
        error_flag = True
        if 'file' not in request.files:
            message = 'No file part'
        else:
            user_file = request.files['file']
            if user_file.filename == '':
                message = 'No file selected for uploading'

            if user_file and allowed_file(user_file.filename):
                filename = secure_filename(user_file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                user_file.save(file_path)
                message = 'File successfully uploaded'
                file_content = open(file_path, 'rb').read()
                hashed_output1 = hash_user_file( file_content)
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

@app.route('/retrieve_file', methods=['POST'])
def retrieve_file():
    if request.method == 'POST':

        message = ''
        error_flag = True

        if request.form['file_hash'] == '':
            message = 'No hash entered'
        #if len(request.form['file_hash']) != 64:
        #   message = 'Incorrect hash '+ request.form['file_hash']
        else:
            error_flag = False
            file_hash = request.form['file_hash']
            file_content = retrieve_from_hash(file_hash)
            message = 'File successfully retrieved'

        if error_flag == True:
            return render_template('second.html', messages = {'message' : message , 'blockchain' : file_content})
        else:
            return render_template('second.html',messages = {'message' : message , 'blockchain' : file_content})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)