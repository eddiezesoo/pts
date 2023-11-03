# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/10

def notify(message, title, msg_type):
    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': title,
            'message': message,
            'sticky': False,  # True 手动关闭   False 延时关闭
            'type': msg_type,
            'next': {'type': 'ir.actions.act_window_close'},
        }
    }

def success(message=None, title='提示'):
    return notify(message, title, 'success')


def danger(message=None, title='提示'):
    return notify(message, title, 'danger')


def warning(message=None, title='提示'):
    return notify(message, title, 'warning')



def warning_tip(message):
    return warning(message)


def danger_tip(message):
    return danger(message)
