from odoo.tests import SingleTransactionCase


class TeacherTest(SingleTransactionCase):
    def test_add_teacher(self):
        teacher = self.env['hr.employee'].create({
            'name': 'Test Teacher',
            'is_teacher': True,

        })

        self.assertRecordValues(teacher, [{'is_teacher': True}])
