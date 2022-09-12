import string
from odoo import models, fields, api
from datetime import datetime


class student(models.Model):
    _name = "student.details"
    _description = "This table contain Student Details "
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="student Name", tracking=True, required=True)
    dateofbirth = fields.Date(String="Date Of Birth", required=True)
    student_img = fields.Image(string="Image")
    age = fields.Integer(String="Age")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    maritalstatus = fields.Selection(
        [('single', 'Single'), ('married', 'Married')], string="Marital Satatus", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    degree_id = fields.Many2one(
        "student.degree", string="Last Degree", required=True, tracking=True)
    degree_pass_year = fields.Char("Degree Passing Year", tracking=True)
    uiversity_id = fields.Many2one(
        "university.details", string="University Name", required=True)
    PCG = fields.Integer(string="Grade", tracking=True)
    course_ids = fields.Many2many(
        'student.courses', string='course', tracking=True)
    company_id = fields.Many2one('res.company', string='company',default=lambda self:self.env.company)
    currency_id = fields.Many2one('res.currency',releted="company_id.currency_id")
    # course_ids = fields.One2many('student.courses', 'student_id', string='course',tracking=True)
    state = fields.Selection([('Inquiry', 'Inquiry'), ('Counselling', 'Counselling'),
                               ('Admission', 'Admission'), ('Canceled', 'Canceled')], string="Stages", default="Inquiry", tracking=True)

    

    @api.onchange('dateofbirth')    
    def _onchange_dateofbirth(self):
        for rec in self:
            if(rec.dateofbirth):
                rec.age = datetime.today().year-rec.dateofbirth.year

    def action_Reopen(self):
        for rec in self:
            rec.state = "Inquiry"
        

    def action_Counselling(self):
        for rec in self:
            rec.state = "Counselling"

    def action_Admission(self):
        for rec in self:
            rec.state = "Admission"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Admited Sucessfully :)',
                'type': 'rainbow_man'
            }
        }

    def action_Canceled(self):
        for rec in self:
            rec.state = "Canceled"
