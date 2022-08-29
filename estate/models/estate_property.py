from copy import copy
from datetime import datetime
from email.policy import default
import string
from typing_extensions import Self
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real state Property adding database"
    # Working fields
    _rec_name = "name"
    name = fields.Text(string="Estate Property Name", required=True)
    status = fields.Char(default="Avaliable", readonly=True, store=True)
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property_type_id")
    description = fields.Text(string="Property Description")
    postcode = fields.Text(string="Property PostCode")
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
    total_area = fields.Integer(
        string="Totel Area", compute="compute_totel_area")
    garden_orientation = fields.Selection([('North', 'Garden is North side'), ('South', 'Garden is South side'), (
        'East', 'Garden is East side'), ('West', 'Garden is West side')], string="Property Garden Orientation")
    # active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [('New', 'New'), ('Offer Received', 'Offer Received'), ('Offer Accepted', 'Offer Accepted'), ('Sold', 'Sold'), ('Canceled', 'Canceled')], required=True, copy=False, default='New')
    salesperson = fields.Many2one('res.users', string='SalesMan',
                                  index=True, tracking=True, default=lambda self: self.env.user)
    buyer = fields.Many2one(
        'res.partner', string="Buyer Name", index=True, tracking=True, copy=False)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    best_price = fields.Text(
        string="Best Price", compute="compute_best_price")

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 1.00)',
         "Expected Price Must be strickly Positive"),
        ('check_selling_price', 'CHECK(selling_price >= 1.00)',
         "Selling Price Must be strickly Positive")]


#python connstrain
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for rec in self:
            if rec.selling_price < rec.expected_price*90/100:
                raise ValidationError("Selling Price must be atlest expected price 90% amount")
                return True
        return True


    # computed Methods
    def compute_totel_area(self):
        for rec in self:
            rec.total_area = self.living_area+self.garden_area

    def compute_best_price(self):
        maxval = []
        for rec in self:
            for i in rec.offer_ids:
                maxval.append(i.price)
        self.best_price = max(maxval) if len(maxval) > 0 else "No Offer"

    @api.onchange('garden')
    def _onchange_garden(self):
        if(self.garden == True):
            self.garden_area = 10
            self.garden_orientation = "North"
        else:
            self.garden_area = ""
            self.garden_orientation = ""

    def action_sold(self):
        for rec in self:
            if rec.status == "Canceled":
                raise UserError("Cancel Property Can't be Sold")
                return True
            rec.status = "Sold"
            break
        return True

    def action_cancel(self):
        for rec in self:
            if rec.status == "Sold":
                raise UserError("Sold Property Can't be Canceled")
                return True
            rec.status = "Canceled"
            break
        return True
