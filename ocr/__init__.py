# Time  ：2022-6-20 17:04
# Author：Houtaroy
import cv2
import numpy as np
from flask import Flask, request
from flask_cors import CORS
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        return {
            "code": 200,
            "message": "识别成功",
            "content": content(request.files['file'])
        }


def content(file):
    ocr_result = ocr.ocr(cv2.imdecode(np.frombuffer(file.read(), dtype=np.uint8), cv2.IMREAD_COLOR))
    return " ".join([line[1][0] for line in ocr_result])
