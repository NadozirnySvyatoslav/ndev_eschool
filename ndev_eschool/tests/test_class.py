from odoo.tests import SingleTransactionCase
from odoo.exceptions import UserError


class ClassTest(SingleTransactionCase):
    def test_add_class(self):
        year = self.env['eschool.year'].create({
            'name': '2023',
        })

        cls = self.env['eschool.class'].create({
            'name': '1-TEST',
            'year_id': year.id,
        })

        self.assertRecordValues(cls, [{'name': '1-TEST'}])
