# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductForm(models.Model):
    _inherit = 'product.product'

    owner_id = fields.Many2one(comodel_name="res.partner", string="Product Owner")
