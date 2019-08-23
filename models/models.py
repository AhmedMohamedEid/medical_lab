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
    lab_test_ids = fields.Many2one(comodel_name="lab.test", string="TEST", )
    lab_result_id = fields.One2many(comodel_name="lab_results", inverse_name="patient_result_id", string="", required=False, )
    #def lab(self):






class LABTEST(models.Model):
    _name = 'lab.test'
    _rec_name = 'name'
    _description = 'Lab Test and Test type'

    name = fields.Char(string="Name", required=True, )
    prefix_code = fields.Char(string="Code", required=True, )
    price = fields.Char(string="Price", required=True, )

    test_content_ids = fields.One2many(comodel_name="lab.test.type", inverse_name="lab_test_id", string="Test Contetn", required=False, )
    test_category_ids = fields.Many2one(comodel_name="lab_category", string="Category Name", required=False, )

class LabTestCategory(models.Model):
    _name = 'lab_category'
    name = fields.Char(string="Category Name", required=False, )

class labrsults(models.Model):
    _name='lab_results'
    name = fields.Char(string="Result", required=False, )
    patient_result_id = fields.Many2one(comodel_name="mdc.lab.patient", string="", required=False, )
    values_result_id = fields.Many2one('lab.test.type')

