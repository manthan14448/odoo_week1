from dataclasses import dataclass
from email.policy import default
import string
from datetime import datetime, timedelta
from tracemalloc import start
from odoo import models, fields


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate_property_offer database"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [("accept", "Accepted"), ('refues', 'Refused')], copy=False)
    partner_id = fields.Many2one(
        'res.partner', string="Patner Name", required=True)
    property_id = fields.Many2one(
        'estate.property', string="Patner id", required=True)
    validity = fields.Integer(string="Validity", default="7")
    date_deadline = fields.Date(compute="compute_date_deadline")

    def compute_date_deadline(self):
        date_1 = ""
        for rec in self:
            start_date = str(rec.property_id.date_availability)
            date_1 = datetime.strptime(
                start_date.replace("-", "/"), "%Y/%m/%d")
            if(rec.validity):
                day = rec.validity
                end_date = date_1 + timedelta(days=day)
                self.date_deadline = end_date
                break
        # start_date = datetime.now()
        # date_compute = datetime.datetime.strptime(start_date, "%m/%d/%y")
        # end_date = date_compute + datetime.timedelta(days=)
