# -*- coding: utf-8 -*-

from odoo import fields, models

class TestRenz(models.Model):
    _name = 'test.renz'
    
    renz = fields.Char(string='Renz')