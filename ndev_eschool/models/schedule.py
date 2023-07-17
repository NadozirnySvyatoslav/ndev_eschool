from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Schedule(models.Model):
    _name = 'eschool.schedule'
    _description = 'Schedule model'

    lesson_id = fields.Many2one(comodel_name="eschool.lesson")
    class_id = fields.Many2one(comodel_name="eschool.class")
    day = fields.Selection(selection=[
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ])