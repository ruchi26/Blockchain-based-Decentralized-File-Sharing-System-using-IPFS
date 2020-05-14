from flask import Flask

UPLOAD_FOLDER = 'F:/main_server/uploads'
DOWNLOAD_FOLDER = 'F:/main_server/downloads'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
