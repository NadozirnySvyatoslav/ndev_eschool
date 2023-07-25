from odoo.tests import SingleTransactionCase


class TimetableTest(SingleTransactionCase):
    def test_add_timetable(self):
        with self._assertRaises(ValueError):
            self.env['eschool.timetable'].create({
                'day': 'Sanday',
            })
