from odoo import models, fields, api


class JournalLine(models.Model):
    _name = 'eschool.journal.line'
    _description = 'Journal record model'

    date = fields.Date(required=True, readonly=True)
    subject_id = fields.Many2one(comodel_name="eschool.subject", required=True,
                                 readonly=True)
    pupil_id = fields.Many2one(comodel_name="res.partner", required=True,
                               readonly=True)
    state = fields.Selection(selection=[
        ('present', 'Present'),
        ('sick', 'Sick'),
        ('fired', 'Fired'),
        ('not_present', 'Not present')
    ], )
    score = fields.Selection([
        ('5', '5 Excellent'),
        ('4', '4 Good'),
        ('3', '3 Not good'),
        ('2', '2 Bad'),
        ('1', '1 Very bad')
    ])
    journal_id = fields.Many2one(comodel_name="eschool.journal", required=True,
                                 readonly=True)
    teacher_id = fields.Many2one(comodel_name="hr.employee", required=True,
                                 readonly=True)


class Journal(models.Model):
    _name = 'eschool.journal'
    _description = 'Journal model'

    name = fields.Char(readonly=True, compute="_compute_name")
    year = fields.Integer(required=True)

    class_id = fields.Many2one(comodel_name="eschool.class", required=True)
    line_ids = fields.One2many(comodel_name="eschool.journal.line",
                               inverse_name="journal_id")
    pupil_ids = fields.One2many(comodel_name="res.partner",
                                inverse_name="class_id", compute="_get_pupils")

    def _get_pupils(self):
        for record in self:
            record.pupil_ids = record.class_id.pupil_ids

    @api.depends('year', 'class_id')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.class_id.name}/{record.year}"

    def action_open(self):
        view_id = self.env.ref('ndev_eschool.open_journal_view_form').id
        return {
            'name': "Open journal",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'eschool.open_journal',
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': {
                'default_journal_id': self.id,
            }
        }
