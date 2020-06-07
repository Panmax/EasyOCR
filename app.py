import uuid

from flask import Flask, jsonify, request
from cnocr import CnOcr

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify(code=-1, message='no file error'), 400
    file = request.files['file']
    file_name = '/tmp/ocr/' + str(uuid.uuid1());
    file.save(file_name)

    ocr = CnOcr()
    ocr_res = ocr.ocr(file_name)
    lines = []
    for line in ocr_res:
        lines.append(''.join(line))
    return jsonify(code=0, message='ok', data=lines)


if __name__ == '__main__':
    app.run()
