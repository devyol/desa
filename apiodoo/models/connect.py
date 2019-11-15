# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xmlrpc.client

username = 'admin@neoethicals.net'
password = 'Mnbvcxzasdfg'
db = 'neo_test'
url = 'http://157.245.240.119:8069'


class conection(models.Model):
    _name = 'odoo.conection'
    _description = 'conection to odoo'

    database = fields.Char(string='Data Base')
    userodoo = fields.Char(string='Usuario Odoo')
    passodoo = fields.Char(string='Password Odoo')
    urlserver = fields.Char(string='Url Server')
    portserver = fields.Char(string='Puerto Server')

    urlcommon = ''
    urlobject = ''
    common = ''
    model = ''
    uid = {}


    def authenticateOdoo(self):
        urlcommon = '{}:{}/xmlrpc/2/common'.format(self.urlserver,self.portserver)
        urlobject = '{}:{}/xmlrpc/2/objcet'.format(self.urlserver,self.portserver)
        common = xmlrpc.client.ServerProxy(urlcommon)
        model = xmlrpc.client.ServerProxy(urlobject)
        uid = common.authenticate(
            self.database,
            self.userodoo,
            self.passodoo,
            {})
        print('respuesta: '+str(uid))
        


    
