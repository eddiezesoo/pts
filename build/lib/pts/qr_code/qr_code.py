# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/7/10
import base64
import qrcode
from io import BytesIO


# create_qr_image_with_code 根据code生成image
def create_qr_image_with_code(qr_code):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_code)
    qr.make(fit=True)
    img = qr.make_image()
    # img.save('/home/zesoo/desktop/test.png')
    # img_file = open('/home/zesoo/desktop/test.png', 'rb').read()
    # return img_file
    temp = BytesIO()
    img.save(temp, format="PNG")
    return base64.b64encode(temp.getvalue())
