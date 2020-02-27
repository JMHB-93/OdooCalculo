from odoo import models, fields

class Peces(models.Model):
    _name = 'pescaderia.panes'
    codigo = fields.Integer('Código', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    temporada = fields.Char('Temporada', required=False)
    precio = fields.Integer()
    cantidadPeces = fields.Integer('Cantidad de Peces', required=True)
    resultado = fields.Integer()
    multiplicar = fields.Integer(compute='multiplicar')
    

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    def suma(self):
        self.resultado = self.cantidadPeces * self.precio
