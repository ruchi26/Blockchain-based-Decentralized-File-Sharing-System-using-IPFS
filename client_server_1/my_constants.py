from flask import Flask

UPLOAD_FOLDER = '/Users/souviksaha/Desktop/Blockchain-based-Decentralized-File-Sharing-System-using-IPFS/client_server_1/uploads'
DOWNLOAD_FOLDER = '/Users/souviksaha/Desktop/Blockchain-based-Decentralized-File-Sharing-System-using-IPFS/client_server_1/downloads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['SERVER_IP'] = '127.0.0.1:5111'
# app.config['NODE_ADDR'] = {'Host' : '127.0.0.2', 'Port' : 5113}
app.config['NODE_ADDR'] = {'Host' : '0.0.0.0', 'Port' : 5113}
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024