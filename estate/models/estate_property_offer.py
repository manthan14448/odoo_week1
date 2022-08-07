from dataclasses import dataclass
from email.policy import default
import string
from datetime import datetime, timedelta
from tracemalloc import start
from odoo import models, fields, api


class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate_property_offer database"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [("accept", "Accepted"), ('refues', 'Refused')], store=True, copy=False, readonly=True)
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

    def action_status_accept(self):
        Accepted_price = 0
        Buyer_id = 0
        for rec in self:
            rec.status = "accept"
            Accepted_price = rec.price
            if rec.partner_id:
                for i in rec.partner_id:
                    Buyer_id = i.id
            if Accepted_price != 0 and Buyer_id != 0:
                for i in rec.property_id:
                    i.selling_price = Accepted_price
                    i.buyer = Buyer_id
                    break
        return True

    def action_status_denied(self):
        for rec in self:
            rec.status = "refues"
            Accepted_price = 0.0
            for i in rec.property_id:
                i.selling_price = Accepted_price
                i.buyer = None
                break
        return True
        # start_date = datetime.now()
        # date_compute = datetime.datetime.strptime(start_date, "%m/%d/%y")
        # end_date = date_compute + datetime.timedelta(days=)
