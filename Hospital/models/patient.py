from datetime import datetime
from email.policy import default
import string
from tokenize import String
from unicodedata import name
from odoo import models, fields


class Patient(models.Model):
    _name = "patient.details"
    _description = "This table contain Patient information"
    _rec_name = "name"
    name = fields.Many2one("res.partner", string="Patient Name", required=True)
    age = fields.Integer(name="Patient Age")
    pre_condition = fields.Char(name="Pre conditions")
    Appoinment_ids = fields.One2many(
        "patient.appoinmet", 'Appoinment_id', string="Appoinments")


class Patient_Appoinment(models.Model):
    _name = "patient.appoinmet"
    _description = "This table contain Patient Appoinmet information"
    doctor_visit = fields.Many2one(
        "doctor.details", required=True, ondelete="cascade")
    visit_date = fields.Date(String="Visiting Data",
                             default=datetime.today(), required=True)
    disease = fields.Char(String="Disease")
    symtoms = fields.Char(String="Symtoms")
    Appoinment_id = fields.Many2one(
        'patient.details', string="Apponment")
