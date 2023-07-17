from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Pupil(models.Model):
    _inherit = 'res.partner'
    _description = 'Pupil model'
    class_id = fields.Many2one(comodel_name="eschool.class")
    is_pupil = fields.Boolean()
    parent_ids = fields.Many2many(comodel_name="res.partner", relation="parent_pupil_rel", column1="pupil_id",
                                  column2="parent_id")
