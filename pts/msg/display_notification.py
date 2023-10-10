# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/10

def success(title, message):
    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': title,
            'message': message,
            'sticky': False,  # True 手动关闭   False 延时关闭
            'type': 'success',
        }
    }

def danger(title, message):
    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': title,
            'message': message,
            'sticky': False,  # True 手动关闭   False 延时关闭
            'type': 'danger',
        }
    }

def warning(title, message):
    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': title,
            'message': message,
            'sticky': False,  # True 手动关闭   False 延时关闭
            'type': 'warning',
        }
    }
