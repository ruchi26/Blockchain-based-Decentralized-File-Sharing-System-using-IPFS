from flask import Flask

<<<<<<< HEAD
UPLOAD_FOLDER = '/Users/souviksaha/Desktop/IPFS users/IPFS_main_server/IPFSUploads'
DOWNLOAD_FOLDER = '/Users/souviksaha/Desktop/IPFS users/IPFS_main_server/IPFSDownloads'

# UPLOAD_FOLDER = 'F:/Blockchain-based-Decentralized-Storage-System/main_server/uploads'
# DOWNLOAD_FOLDER = 'F:/Blockchain-based-Decentralized-Storage-System/main_server/downloads'

=======
UPLOAD_FOLDER = '/Users/souviksaha/Desktop/IPFSUploads'
DOWNLOAD_FOLDER = '/Users/souviksaha/Desktop/IPFSDownloads'
>>>>>>> front-end
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
