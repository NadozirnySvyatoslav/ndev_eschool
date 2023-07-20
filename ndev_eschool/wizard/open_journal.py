from odoo import models, fields


class OpenJournal(models.TransientModel):
    _name = "eschool.open_journal"
    _description = "Provide fulfil date, pupils, subject in journal line"

    journal_id = fields.Many2one(comodel_name="eschool.journal")
    subject_id = fields.Many2one(comodel_name="eschool.subject")
    teacher_id = fields.Many2one(comodel_name="hr.employee",
                                 domain=[('is_teacher', '=', True)])
    date = fields.Date(default=fields.Datetime.now)

    def action_open(self):
        line_model = self.env["eschool.journal.line"]
        journal = self.env["eschool.journal"].browse(self.journal_id.id)
        pupils = self.env["res.partner"].search(
            [('is_pupil', '=', True), ('class_id', '=', journal.class_id.id)])

        for pupil in pupils:
            line = line_model.search([
                ('date', '=', self.date),
                ('subject_id', '=', self.subject_id.id),
                ('journal_id', '=', self.journal_id.id),
                ('pupil_id', '=', pupil.id),
            ])
            if not line:
                line_model.create({
                    "date": self.date,
                    "subject_id": self.subject_id.id,
                    "teacher_id": self.teacher_id.id,
                    "journal_id": self.journal_id.id,
                    "pupil_id": pupil.id,
                })

        view_id = self.env.ref(
            'ndev_eschool.eschool_journal_line_tree_view').id
        return {
            'name': f"{self.subject_id.name} {self.date} "
                    f"{self.teacher_id.name}",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'eschool.journal.line',
            'view_id': view_id,
            'views': [(view_id, 'tree')],
            'target': 'fullscreen',
            'context': {},
            'domain': [('journal_id', '=', self.journal_id.id),
                       ('subject_id', '=', self.subject_id.id),
                       ("date", '=', self.date)
                       ],
        }
