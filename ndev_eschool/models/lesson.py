from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Lesson(models.Model):
    _name = 'eschool.lesson'
    _description = 'Lesson model'

    name = fields.Char()