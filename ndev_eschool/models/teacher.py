from odoo import models, fields


class Teacher(models.Model):
    """
    Inherited class for teachers
    """
    _inherit = 'hr.employee'
    _description = 'Teacher model'
    is_teacher = fields.Boolean()
    subject_ids = fields.Many2many(comodel_name="eschool.subject",
                                   relation="teacher_subject_rel",
                                   column2="subject_id",
                                   column1="teacher_id")
