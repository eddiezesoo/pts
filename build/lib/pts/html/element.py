# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2022/05/01 20


def hide(wrapper):
    def wrap(*args):
        return """
        <style>
            {} {{
                display: none !important;
            }}
        </style>
        """.format(', '.join(args)) if (len(args) != 0 and wrapper(*args)) else False

    return wrap
