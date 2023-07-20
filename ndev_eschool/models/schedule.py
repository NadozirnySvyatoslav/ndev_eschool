from odoo import models, fields, api


class Schedule(models.Model):
    _name = 'eschool.schedule'
    _description = 'Schedule model'
    date = fields.Date()
    class_id = fields.Many2one(comodel_name="eschool.class")
    subject_id = fields.Many2one(comodel_name="eschool.subject")
    teacher_id = fields.Many2one(comodel_name="hr.employee", domain=[('is_teacher', '=', True)])


class TimetableLine(models.Model):
    _name = 'eschool.timetable.line'
    _description = 'Timetable line model'
    _order = 'order'

    name = fields.Char(compute="_compute_name")
    order = fields.Integer(required=True)

    subject_id = fields.Many2one(comodel_name="eschool.subject", required=True)
    teacher_id = fields.Many2one(comodel_name="hr.employee", domain=[('is_teacher', '=', True)], required=True)
    timetable_id = fields.Many2one(comodel_name="eschool.timetable", required=True)
    periodically = fields.Selection(selection=[
        ('weekly', 'Weekly'),
        ('odd', 'Odd week'),
        ('even', 'Even week'),
    ], required=True)

    @api.onchange('subject_id', 'teacher_id')
    def _compute_name(self):
        for r in self:
            r.name = f"{r.order} / {r.subject_id.name} / {r.teacher_id.name}"


class Timetable(models.Model):
    _name = 'eschool.timetable'
    _description = 'Timetable model'

    line_ids = fields.One2many(comodel_name="eschool.timetable.line", inverse_name="timetable_id")
    class_id = fields.Many2one(comodel_name="eschool.class", required=True)
    day = fields.Selection(selection=[
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ], required=True)

