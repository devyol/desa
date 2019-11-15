# -*- coding: utf-8 -*-
from odoo import http

# class Apiodoo(http.Controller):
#     @http.route('/apiodoo/apiodoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apiodoo/apiodoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apiodoo.listing', {
#             'root': '/apiodoo/apiodoo',
#             'objects': http.request.env['apiodoo.apiodoo'].search([]),
#         })

#     @http.route('/apiodoo/apiodoo/objects/<model("apiodoo.apiodoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apiodoo.object', {
#             'object': obj
#         })