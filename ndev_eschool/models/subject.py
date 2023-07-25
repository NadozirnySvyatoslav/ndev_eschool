from odoo import models, fields


class Subject(models.Model):
    """
    Class for subjects
    """
    _name = 'eschool.subject'
    _description = 'Subject such as math, chemistry, physics'
    name = fields.Char()
    teacher_ids = fields.Many2many(comodel_name="hr.employee",
                                   relation="teacher_subject_rel",
                                   column1="subject_id",
                                   column2="teacher_id")
