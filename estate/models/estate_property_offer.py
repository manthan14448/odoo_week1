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
