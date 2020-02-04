# -*- coding: utf-8 -*-

from odoo import fields, models


class PartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    level = fields.Char(string='Level')