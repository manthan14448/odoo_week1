from copy import copy
from datetime import datetime
from email.policy import default
import string
from typing_extensions import Self
from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real state Property adding database"
    # Working fields
    name = fields.Char(string="Estate Property Name", required=True)
    description = fields.Text(string="Property Description")
    postcode = fields.Char(string="Property PostCode")
    date_availability = fields.Date(
        string="Propery Date of Availability", copy=False, default=datetime.today())
    expected_price = fields.Float(
        string="Property Expected Selling Price", required=True)
    selling_price = fields.Float(
        string="Property Real Selling Price", copy=False, readonly=True)
    bedrooms = fields.Integer(string="Property Totel Bedrooms", default="2")
    living_area = fields.Integer(string="Property Living area")
    facades = fields.Integer(string="Property facades")
    garage = fields.Boolean(string="Property Has Garage Yes or No")
    garden = fields.Boolean(string="Property Has Garden Yes or No")
    garden_area = fields.Integer(string="Property Has Gardern area Yes or No")
    garden_orientation = fields.Selection([('North', 'Garden is North side'), ('South', 'Garden is South side'), (
        'East', 'Garden is East side'), ('West', 'Garden is West side')], string="Property Garden Orientation")
    active = fields.Boolean(string="Active", default=False)
