## EasyOCR

> EasyOCR 是基于 [cnocr](https://github.com/breezedeus/cnocr) 简单封装的 OCR 识别接口
> 
> 真的是简单封装😂


### Usage

```shell
# python version >= 3.4
pip install -r requirements.txt
python app.py

# Or use docker
docker run -d --name easy-ocr --restart=always -p 5000:5000 panmax/easy-ocr
```

![samples/2.png](samples/2.png)

测试图片见 [samples/1.png](samples/1.png)

![samples/2.png](samples/4.png)

测试图片见 [samples/3.png](samples/3.png)