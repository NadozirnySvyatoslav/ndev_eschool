from datetime import datetime
from odoo.tests import SingleTransactionCase
from odoo.exceptions import UserError
from odoo.tests.common import Form


class JournalTest(SingleTransactionCase):
    def test_add_journal(self):
        year = self.env['eschool.year'].create({
            'name': '2023',
        })

        pupil = self.env['res.partner'].create({
            'name': 'Test Pupil',
            'is_pupil': True,
            'birth': '2010-01-01',
        })

        cls = self.env['eschool.class'].create({
            'name': '1-TEST',
            'year_id': year.id,
            'pupil_ids': [pupil.id],
        })

        j = self.env['eschool.journal'].create({
            'class_id': cls.id,
            'year': 2023,
        })

        teacher = self.env['hr.employee'].create({
            'name': 'Test Teacher',
            'is_teacher': True,

        })

        subj = self.env['eschool.subject'].create({
            'name': 'Test Subject',
        })

        open_form = self.env["eschool.open_journal"].create({
            'teacher_id': teacher.id,
            'journal_id': j.id,
            'subject_id': subj.id,
            'date': datetime.now(),
        })
        open_form.action_open()
