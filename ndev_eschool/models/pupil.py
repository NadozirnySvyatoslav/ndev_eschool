from odoo import models, fields, api


class Pupil(models.Model):
    """
    Inherited class for pupils
    """
    _inherit = 'res.partner'
    _description = 'Pupil model'

    class_id = fields.Many2one(comodel_name="eschool.class", store=True)
    is_pupil = fields.Boolean()
    parent_ids = fields.Many2many(comodel_name="res.partner",
                                  relation="parent_pupil_rel",
                                  column1="pupil_id",
                                  column2="parent_id")
    year_id = fields.Many2one(comodel_name="eschool.year",
                              compute="_compute_year", store=True)

    @api.depends('class_id')
    def _compute_year(self):
        for record in self:
            if record.class_id:
                record.year_id = record.class_id.year_id
            else:
                record.year_id = None
