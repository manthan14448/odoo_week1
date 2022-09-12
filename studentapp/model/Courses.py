from email.policy import default
from re import S
import string
from odoo import models,fields

class Courses(models.Model):
    _name= "student.courses"
    _description = "This table contain Student Details "

    _rec_name="course_name"
    course_name = fields.Char(name="Courses Name",requried=True)
    student_id = fields.Many2one('student.details', string='student')
    currency_id = fields.Many2one('res.currency',releted="student_id.currency_id")
    courses_fees = fields.Monetary(name="Courses Fees")
    duration=fields.Selection([('1','One'),('2','Two'),('3','Three'),('4','Four'),('5','Five')],string="Duration")
    eligibility=fields.Selection([('10th','10th'),('12th','12th'),('Graduate','Graduate'),('Post_Graduate','Post Graduate'),('Graduate','PHD')],name="Courses Eligibility",required=True    )
    color = fields.Integer(string="Color")
    cut_off=fields.Float(name="Courses Cut Off")