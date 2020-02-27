from odoo import models, fields

class Proveedores(models.Model):
    _name = 'pescaderia.proveedores'
    codigo = fields.Integer('Código', required=True)
    nombre = fields.Char('Nombre', required=True)
    nombreRep = fields.Char('Nombre Representante', required=True)
    telefono = fields.Char('Teléfono', required=True)
    diasVisita = fields.Char('Días que Visita', required=False)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
