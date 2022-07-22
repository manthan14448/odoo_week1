import string
from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real state Property adding database"
    # Working fields
    name = fields.Char(string="Property Name")
    description = fields.Text(string="Property Description")
    postcode = fields.Char(string="Property PostCode")
    date_availability = fields.Date(string="Propery Due Date")
    expected_price = fields.Float(string="Property Expected Selling Price")
    selling_price = fields.Float(string="Property Real Selling Price")
    bedrooms = fields.Integer(string="Property Totel Bedrooms")
    living_area = fields.Integer(string="Property Living area")
    facades = fields.Integer(string="Property facades")
    garage = fields.Boolean(string="Property Has Garage Yes ot No")
    garden = fields.Boolean(string="Property Has Garage Yes ot No")
    garden_area = fields.Integer(string="Property Has Gardern area Yes or No")
    garden_orientation = fields.Selection([('North', 'Garden is North side'), ('South', 'Garden is South side'), (
        'East', 'Garden is East side'), ('West', 'Garden is West side')], string="Property Garden Orientation")
