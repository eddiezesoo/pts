# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2022/05/01 20
from pts.author import info
from pts.html.element import hide


@hide
def t1(*args):
    return True


def t2():
    @hide
    def t2_2(*args):
        return True

    return t2_2('.btn', '#btn')


print(t1('.btn', '#abc', info.NAME, info.EMAIL))
print(t2())
