from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Journal(models.Model):
    _name = 'eschool.journal'
    _description = 'Journal model'

    date = fields.Date()
    lesson_id = fields.Many2one(comodel_name="eschool.lesson")
    pupil_id = fields.Many2one(comodel_name="res.partner")
    state = fields.Selection(selection=[('present','Present'),('not_present','Not present')])
    score = fields.Integer()


