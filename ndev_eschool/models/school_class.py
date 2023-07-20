from odoo import models, fields


class SchoolYear(models.Model):
    _name = 'eschool.year'
    _description = 'Year model'
    name = fields.Char(required=True)
    class_ids = fields.One2many(comodel_name="eschool.class",
                                inverse_name="year_id")


class SchoolClass(models.Model):
    _name = 'eschool.class'
    _description = 'Class model'
    name = fields.Char(required=True)
    year_id = fields.Many2one(comodel_name="eschool.year", required=True)
    curator_id = fields.Many2one(comodel_name="hr.employee")
    pupil_ids = fields.One2many(comodel_name="res.partner",
                                inverse_name="class_id", string="Pupils")
