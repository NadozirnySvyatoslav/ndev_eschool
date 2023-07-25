from odoo import models, fields


class Parent(models.Model):
    """
    Inherited class for Parents of pupils
    """
    _inherit = 'res.partner'
    _description = 'Parent model'
    is_parent = fields.Boolean()
    pupil_ids = fields.Many2many(comodel_name="res.partner",
                                 relation="parent_pupil_rel",
                                 column1='parent_id',
                                 column2='pupil_id')
    relation = fields.Selection(
        selection=[
            ('mother', 'Mother'),
            ('father', 'Father'),
            ('grandmother', 'Grandmother'),
            ('grandfather', 'Grandfather'),
            ('curator', 'Curator'),
        ]
    )
