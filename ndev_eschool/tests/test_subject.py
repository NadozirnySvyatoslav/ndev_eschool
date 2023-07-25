from odoo.tests import SingleTransactionCase


class SubjectTest(SingleTransactionCase):
    def test_add_subject(self):
        s = self.env['eschool.subject'].create({
            'name': 'Test Subject',
        })

        self.assertRecordValues(s, [{'name': 'Test Subject'}])
