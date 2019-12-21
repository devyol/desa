# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning
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

    def param(self):
        urlcommon = '{}:{}/xmlrpc/2/common'.format(self.urlserver,self.portserver)
        urlobject = '{}:{}/xmlrpc/2/object'.format(self.urlserver,self.portserver)
        common = xmlrpc.client.ServerProxy(urlcommon)
        objectr = xmlrpc.client.ServerProxy(urlobject)
        param = {'common':common,'object':objectr}
        return param

    def get_uid(self):
        common = self.param()['common']
        uid = common.authenticate(self.database,self.userodoo,self.passodoo,{})
        return uid


    def testvar(self):
        try:
            uid = self.get_uid()
            print('Conexion exitosa, uid: ' + str(uid))            
        except Exception as ex:
            print(ex)


        
        
        
        
