# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/10/20

# 周岁计算
# 规定：过了生日算1周岁，如1月1日生，次年1月2日算满1周岁
def full_year(start_date, end_date):
    if start_date.month * 100 + start_date.day < end_date.month * 100 + end_date.day:
        return end_date.year - start_date.year
    else:
        return end_date.year - start_date.year - 1
