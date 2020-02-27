from odoo import models, fields

class Embasados(models.Model):
    _name = 'pescaderia.embasados'
    codigo = fields.Integer('Código', required=True)
    nombre = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca', required=True)
    precio = fields.Float('Precio', required=True)
