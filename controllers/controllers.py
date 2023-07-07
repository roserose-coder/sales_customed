# -*- coding: utf-8 -*-
# from odoo import http


# class SalesCustomed(http.Controller):
#     @http.route('/sales_customed/sales_customed', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_customed/sales_customed/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_customed.listing', {
#             'root': '/sales_customed/sales_customed',
#             'objects': http.request.env['sales_customed.sales_customed'].search([]),
#         })

#     @http.route('/sales_customed/sales_customed/objects/<model("sales_customed.sales_customed"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_customed.object', {
#             'object': obj
#         })
