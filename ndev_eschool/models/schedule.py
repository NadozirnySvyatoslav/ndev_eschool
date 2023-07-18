from odoo import models, fields


class Schedule(models.Model):
    _name = 'eschool.schedule'
    _description = 'Schedule model'

    subject_id = fields.Many2one(comodel_name="eschool.subject")
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
    periodically = fields.Selection(selection=[
        ('weekly', 'Weekly'),
        ('odd', 'Odd week'),
        ('even', 'Even week'),
    ])
