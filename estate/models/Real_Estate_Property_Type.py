
from odoo import models
from odoo import fields


class realstatetype(models.Model):
    _name = "estate.property.type"
    _description = "Real state Property Type database"
    _oder = "name asc"
    name = fields.Char(string="Real state Property Type", required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='property_ids')

    _sql_constraints = [
        ('Property_tag_name', 'unique(name)', "The Name Must Be Unique")
    ]
