# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/20

def full_year(start_date, end_date):
    if start_date.month * 100 + start_date.day < end_date.month * 100 + end_date.day:
        return end_date.year - start_date.year
    else:
        return end_date.year - start_date.year - 1
