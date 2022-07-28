import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = "doctor.details"
    _description = "This table contain doctor information"

    _rec_name = "name"
    name = fields.Many2one("res.partner", string="Doctor Name", required=True)
    degree = fields.Char(string="Doctor Degree Info",
                         name="Degree", required=True)
    degree_info = fields.Many2many("doctor.degree")
    speciality = fields.Selection(
        [('ear', 'Ear'), ('nose', 'Nose'), ('brain', 'Brain')], name="Speciality", required=True)
    number = fields.Char(string="Uniq number", required=True)

    @api.constrains('number')
    def _check_mobile_unique(self):
        number_counts = self.search_count(
            [('number', '=', self.number), ('id', '!=', self.id)])
        if number_counts > 0:
            raise ValidationError(
                "number already exists!\nPlease use different number")


class Doctor_degree(models.Model):
    _name = "doctor.degree"
    _description = "This table contain doctor degree"

    degrees = fields.Char(string="Doctor Degree Info",
                          name="Degree", required=True)
