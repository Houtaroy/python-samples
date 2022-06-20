# OCR

使用[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

结合Flask搭建为Web接口, 支持跨域

## 上传文件

使用Http请求上传的文件, 不满足PaddleOCR的识别参数要求

通过阅读源码将其转换为ndarray即可:

```python
import cv2
import numpy as np
from flask import request

file = request.files['file']
cv2.imdecode(np.frombuffer(file.read(), dtype=np.uint8), cv2.IMREAD_COLOR)
```