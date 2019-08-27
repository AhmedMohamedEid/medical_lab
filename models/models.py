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
    # lab_test_ids = fields.Many2one(comodel_name="lab.test", string="TEST", )
    # lab_result_id = fields.One2many(comodel_name="lab_results", inverse_name="patient_result_id", string="", required=False,)
    # price_count = fields.Char(string='Sum' , compute='price_sum')
    #
    # @api.depends('lab_result_id')
    # def price_sum(self):
    #     result = 0
    #     for record in self.lab_result_id:
    #         result = result+record.lab_test_id.price
    #     self.price_count=result
    #



