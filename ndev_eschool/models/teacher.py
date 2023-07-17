from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TeacherSubject(models.Model):
    _name = 'eschool.subject.teacher'
    _description = 'Teacher subjects model'
    subject_id = fields.Many2one(comodel_name="eschool.subject")
    teacher_id = fields.Many2one(comodel_name="hr.employee")


class Teacher(models.Model):
    _inherit = 'hr.employee'
    _description = 'Teacher model'
    is_teacher = fields.Boolean()
    #subject_ids = fields.One2many(comodel_name="eschool.subject.teacher", inverse_name="teacher_id", string="Subjects")
    subject_ids = fields.Many2many(comodel_name="eschool.subject", relation="teacher_subject_rel", column2="subject_id",
                                   column1="teacher_id")
