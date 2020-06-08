import uuid

from flask import Flask, jsonify, request
from cnocr import CnOcr
from cnstd import CnStd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify(code=-1, message='no file error'), 400
    file = request.files['file']

    _uuid = str(uuid.uuid1())
    file_name = '/tmp/ocr/' + _uuid
    file.save(file_name)

    ocr = CnOcr(name=_uuid)
    std = CnStd(name=_uuid)
    box_info_list = std.detect(file_name)

    lines = []
    for box_info in box_info_list:
        cropped_img = box_info['cropped_img']  # 检测出的文本框
        ocr_res = ocr.ocr_for_single_line(cropped_img)
        lines.append(''.join(ocr_res))
    return jsonify(code=0, message='ok', data=lines)


if __name__ == '__main__':
    app.run()
