# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/7/12

def act_url_with_ids(attach_ids, attachment_type='png'):
    return {
        'name': '下载',
        'type': 'ir.actions.act_url',
        'url': '/downloader/{}/{}'.format(attachment_type, attach_ids),
        'target': 'self',
    }
