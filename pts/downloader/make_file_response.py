# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/7/11
import base64
import io
import logging
import zipfile

from odoo.http import content_disposition, request

_logger = logging.getLogger(__name__)


def make_file_response(zip_filename, attachments, attachment_type):
    stream = io.BytesIO()
    try:
        with zipfile.ZipFile(stream, 'w') as doc_zip:
            for attachment in attachments:
                if attachment.type in ['url', 'empty']:
                    continue
                filename = '{}.{}'.format(attachment.res_name, attachment_type)
                doc_zip.writestr(str(filename), base64.b64decode(attachment['datas']),
                                 compress_type=zipfile.ZIP_DEFLATED)
    except zipfile.BadZipfile:
        _logger.exception("BadZipfile exception")
    content = stream.getvalue()
    headers = [
        ('Content-Type', 'zip'),
        ('X-Content-Type-Options', 'nosniff'),
        ('Content-Length', len(content)),
        ('Content-Disposition', content_disposition(zip_filename))
    ]
    return request.make_response(content, headers)
