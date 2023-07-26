from datetime import datetime
from odoo import models, fields, api


class Person(models.Model):
    """
    Basic class with name, age, gender fields for partners
    """
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
        for r in self:
            r.name = (f"{r.surname if r.surname else 'Noname'} "
                      f"{r.first_name if r.first_name else ''} "
                      f"{r.second_name if r.second_name else ''}"
                      ).strip()

    @api.depends('birth')
    def _compute_age(self):
        for record in self:
            if not record.birth:
                record.age = 0
            else:
                current_date = datetime.now()
                record.age = current_date.year - record.birth.year
