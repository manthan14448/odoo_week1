from odoo import models,fields

class Duration(models.Model):
    _name= "student.courses.duration"
    _description = "This table contain Student Courses Duration "
    name=fields.Selection([('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five')],string="Duration")