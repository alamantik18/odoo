# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class Persons(models.Model):
    _name = 'company.persons'
    _description = 'Persons which have belong to companies'

    first_name = fields.Char(string='Person`s first name', required=True)
    last_name = fields.Char(string='Person`s last name', required=True)
    full_name = fields.Char(string='Person`s full name', required=True, readonly=True, compute='_set_full_name')
    birthday = fields.Date(string='Birth Date', help='Select your birth date.')
    age = fields.Char(string='Person`s age', readonly=True, compute='_set_age')
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
                                 reqired=True, default=lambda self: self.env.company)
    sex = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non binary'),
    ])

    @api.onchange('first_name', 'last_name')
    def _set_full_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.full_name = record.first_name + ' ' + record.last_name

    @api.onchange('birthday')
    def _set_age(self):
        for record in self:
            if record.birthday:
                result_age = relativedelta(date.today(), record.birthday)
                record.age = str(result_age.years) + ' years'

    @api.constrains('birthday')
    def _check_future_date(self):
        for record in self:
            if record.birthday >= date.today():
                raise ValidationError('Future dates in birthday field are not allowed.')
