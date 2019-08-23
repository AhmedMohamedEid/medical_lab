# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MDCLABPATIENT(models.Model):
    _name = 'mdc.lab.patient'
    _rec_name = 'name'
    _description = 'Patient Profile'

    name = fields.Char(string="Name", required=True, )
    image = fields.Binary(string="Image",)
    title = fields.Many2one('res.partner.title')
    patient_id = fields.Char(string="Patient ID", required=False, )
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'),], required=True, )
    email = fields.Char(string="Email", required=False, )
    age = fields.Integer(string="Age", required=True,)
    address = fields.Char(string="Address", required=False, )
    phone = fields.Char(string="Phone", required=True, )
    blood_group = fields.Selection(string="Blood Group", selection=[('b_pve', 'B+ve'),('b_nve', 'B-ve'),
                                                                    ('a_nve', 'A-ve'),('a_pve', 'A+ve'),
                                                                    ('ab_pve', 'AB+ve'), ('ab_nve', 'AB-ve'),
                                                                    ('o', 'O'), ], required=False, )
    note = fields.Text(string="Note", required=False, )




class LABTEST(models.Model):
    _name = 'lab.test'
    _rec_name = 'name'
    _description = 'Lab Test and Test type'

    # name = fields.Char()
