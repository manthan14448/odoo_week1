
from odoo import models, fields


class estate_property_tag(models.Model):
    _name = "estate.property.tag"
    _oder = "name asc"
    _description = "estate_property_tag database"
    name = fields.Char(string="Name", required=True)
