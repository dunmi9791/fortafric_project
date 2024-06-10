from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import date


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    project_id = fields.Many2one('project.project', string='Project')


class ProjectProject(models.Model):
    _inherit = 'project.project'

    purchase_ids = fields.One2many('purchase.order', 'project_id', string='Procurements')
    purchase_count = fields.Integer(
        string='Purchase Count', compute='_compute_purchase_count'
    )

    @api.depends('requisition_ids')
    def _compute_purchase_count(self):
        for project in self:
            project.purchase_count = len(project.purchase_ids)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_technical_assistant = fields.Boolean(string='Technical Assistant', default=False)
