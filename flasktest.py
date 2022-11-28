
import os
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import read
import qr
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg',])
UPLOAD_FOLDER = os.path.realpath(os.path.dirname(__file__))+'/upload'
if not os.path.exists(UPLOAD_FOLDER):
    print("path", UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
print("File location using os.getcwd():", os.getcwd())

print(
    f"File location using __file__ variable: {os.path.realpath(os.path.dirname(__file__))}")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def get_route():
    resp = jsonify({'message': 'Welcome to Aadhar Pan'})
    resp.status_code = 400
    return resp


@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = read.read_data(UPLOAD_FOLDER+"/"+filename)
        resp = jsonify({'message': 'File successfully uploaded', "data": data})
        resp.status_code = 201
        os.remove(UPLOAD_FOLDER+"/"+filename)
        return resp
    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


@app.route('/qrAadhar', methods=['POST'])
def upload_qr():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = qr.qr_aadhar(UPLOAD_FOLDER+"/"+filename)
        resp = jsonify({'message': 'File successfully uploaded', "data": data})
        resp.status_code = 201
        os.remove(UPLOAD_FOLDER+"/"+filename)
        return resp
    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(port=5002)
