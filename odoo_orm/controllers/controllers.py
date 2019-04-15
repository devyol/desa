# -*- coding: utf-8 -*-
from odoo import http

# class /home/erik/misModulos/desa/odooOrm(http.Controller):
#     @http.route('//home/erik/mis_modulos/desa/odoo_orm//home/erik/mis_modulos/desa/odoo_orm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/erik/mis_modulos/desa/odoo_orm//home/erik/mis_modulos/desa/odoo_orm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/erik/mis_modulos/desa/odoo_orm.listing', {
#             'root': '//home/erik/mis_modulos/desa/odoo_orm//home/erik/mis_modulos/desa/odoo_orm',
#             'objects': http.request.env['/home/erik/mis_modulos/desa/odoo_orm./home/erik/mis_modulos/desa/odoo_orm'].search([]),
#         })

#     @http.route('//home/erik/mis_modulos/desa/odoo_orm//home/erik/mis_modulos/desa/odoo_orm/objects/<model("/home/erik/mis_modulos/desa/odoo_orm./home/erik/mis_modulos/desa/odoo_orm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/erik/mis_modulos/desa/odoo_orm.object', {
#             'object': obj
#         })