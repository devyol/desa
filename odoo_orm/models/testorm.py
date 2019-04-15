# -*- coding: utf-8 -*-

from odoo import models, fields, api


class operaciones(models.Model):
    _name = 'persona'
    _description = 'Modulo Demo para utilizar operaciones ORM'
    
    name = fields.Char(string='Nombre')
    edad = fields.Integer(string = 'Edad')
    email = fields.Char(string='email')
    celular = fields.Char(string='Celular')
    direccion = fields.Char(String='Direccion')
    
    def accept(self):
        
        #funcion que seleccione un objeto
        
        self.env
        
        
        

# class /home/erik/mis_modulos/desa/odoo_orm(models.Model):
#     _name = '/home/erik/mis_modulos/desa/odoo_orm./home/erik/mis_modulos/desa/odoo_orm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100