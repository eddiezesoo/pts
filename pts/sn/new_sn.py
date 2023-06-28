# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/6/28


def sn2(sn, count):
    return '{}.{:02d}'.format(sn, count + 1)

def sn3(sn, count):
    return '{}.{:03d}'.format(sn, count + 1)

def sn2_(sn, count):
    return '{}_{:02d}'.format(sn, count + 1)

def sn3_(sn, count):
    return '{}_{:03d}'.format(sn, count + 1)
