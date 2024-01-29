# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/10

def notify(message, title, msg_type, close, next_act):
    msg = {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': title,
            'message': message,
            'sticky': False,  # True 手动关闭   False 延时关闭
            'type': msg_type,
        }
    }
    if close:
        # 后续关闭动作，可以是其他动作
        msg.get('params').update({'next': {'type': 'ir.actions.act_window_close'}})
    if next_act:
        # 后续关闭动作，可以是其他动作
        msg.get('params').update({'next': next_act})
    return msg

def success(message=None, title='提示', close=False, next_act=None):
    return notify(message, title, 'success', close, next_act)


def danger(message=None, title='提示', close=False, next_act=None):
    return notify(message, title, 'danger', close, next_act)


def warning(message=None, title='提示', close=False, next_act=None):
    return notify(message, title, 'warning', close, next_act)



def warning_tip(message):
    return warning(message)


def danger_tip(message):
    return danger(message)
