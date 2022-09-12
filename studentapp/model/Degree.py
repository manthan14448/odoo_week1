from odoo import models,fields

class Degree(models.Model):
    _name= "student.degree"
    _description = "This table contain Student Details "
    _rec_name="degree_name"
    degree_name = fields.Char(name="Degree Name",required=True)
    degree_code = fields.Char(name="Degree Code",required=True)