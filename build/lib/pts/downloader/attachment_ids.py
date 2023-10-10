# -*- coding: utf-8 -*-
# Author zhuangyisheng@qq.com 2023/7/12

def join_ids_with_res_arg(e, res_model, res_field, res_ids):
    return ','.join([str(a.id) for a in e.env['ir.attachment'].search(
        [('res_model', '=', res_model), ('res_field', '=', res_field), ('res_id', 'in', res_ids)])])
