
from odoo import models
from odoo import fields


class realstatetype(models.Model):
    _name = "estate.property.type"
    _description = "Real state Property Type database"
    name = fields.Char(string="Real state Property Type", required=True)
