from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SchoolClass(models.Model):
    _name = 'eschool.class'
    _description = 'Class model'
    name = fields.Char()
    year = fields.Integer()
    curator_id = fields.Many2one(comodel_name="hr.employee")
    pupil_ids = fields.One2many(comodel_name="res.partner", inverse_name="class_id", string="Pupils")
