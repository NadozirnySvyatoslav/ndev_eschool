from odoo.tests import SingleTransactionCase


class ParentTest(SingleTransactionCase):
    def test_add_parent(self):
        teacher = self.env['res.partner'].create({
            'name': 'Test Parent',
            'is_parent': True,
        })

        self.assertRecordValues(teacher, [{'is_parent': True}])
