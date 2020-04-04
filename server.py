import os
import urllib.request
import ipfshttpclient
from my_constants import app
from flask import Flask, flash, request, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def hashed(filename):
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    hashed_file = client.add(filename)['Hash']
    return  hashed_file

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            hashed_output1 = hashed(filename)
            flash(hashed_output1)
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)