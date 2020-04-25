from flask import Flask

UPLOAD_FOLDER = 'F:/Blockchain-based-Decentralized-Storage-System/uploads'
DOWNLOAD_FOLDER = 'F:/Blockchain-based-Decentralized-Storage-System/downloads'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
