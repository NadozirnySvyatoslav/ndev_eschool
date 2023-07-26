from datetime import datetime
from odoo.tests import SingleTransactionCase


class PupilTest(SingleTransactionCase):
    def test_add_pupil(self):
        pupil = self.env['res.partner'].create({
            'name': 'Test Pupil',
            'is_pupil': True,
            'birth': '2010-01-01',
        })
        current_date = datetime.now()
        age = current_date.year - 2010
        self.assertRecordValues(pupil, [{'age': age}])
