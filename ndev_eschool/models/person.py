from datetime import datetime
from odoo import models, fields, api


class Person(models.Model):
    _inherit = 'res.partner'
    _description = 'Add names and age to partner model'

    first_name = fields.Char()
    second_name = fields.Char()
    surname = fields.Char()

    birth = fields.Date()
    age = fields.Integer(compute="_compute_age")
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
    ])

    @api.onchange('first_name', 'second_name', 'surname')
    def _on_change_name(self):
        for record in self:
            record.name = (f"{record.surname if record.surname else 'Noname'} "
                           f"{record.first_name if record.first_name else ''} "
                           f"{record.second_name if record.second_name else''}"
                           ).strip()

    @api.depends('birth')
    def _compute_age(self):
        for record in self:
            if not record.birth:
                record.age = 0
            else:
                current_date = datetime.now()
                record.age = current_date.year - record.birth.year
