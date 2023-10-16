# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/10

def success(message=None, title='提示'):
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


def danger(message=None, title='提示'):
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


def warning(message=None, title='提示'):
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


def warning_tip(message):
    return warning(message)


def danger_tip(message):
    return danger(message)
