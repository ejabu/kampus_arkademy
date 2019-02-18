from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliahTopik(models.Model):
    _name = 'kampus.kuliah.topik'
    _order = "sequence"

    sequence = fields.Integer('Sequence')
    name = fields.Char('Name')
