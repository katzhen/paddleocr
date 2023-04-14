import os
from flask import Flask
from flask import request
from flask import jsonify
from paddleocr import PaddleOCR

app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True,lang='ch',use_gpu=False)

@app.route('/', methods=['POST'])
def index():
    if request.method != 'POST':
        return "method must be POST"
    if 'file' not in request.files:
        return "no file part"
    file = request.files['file']
    if file.filename == '':
        return "no selected file"
    path = os.path.join("/paddle",file.filename)
    file.save(path)
    result = ocr.ocr(path, cls=True)
    res = []
    for idx in range(len(result)):
        txts = [line[1][0] for line in result[idx]]
        res.append(txts)
    return jsonify(res);

if __name__ == '__main__':
    # app.run(host,port,debug,options)
    # 默认值：host="127.0.0.1",port=5000,debug=False
    app.run(host="0.0.0.0", port=5000)
