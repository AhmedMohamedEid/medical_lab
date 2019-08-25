from odoo import api, fields, models

class LABCONTENT(models.Model):
    _name = 'lab.test.type'
    _rec_name = 'name'
    _description = 'Lab Test Type'

    name = fields.Char(string="Name", required=True, )
    lab_test_id = fields.Many2one(comodel_name="lab.test", string="Lab Test", required=True, )
    result = fields.Char(string="result", required=False, )

    ref_intervals = fields.Char(string="Normal Range", required=False, )
    test_unit_id = fields.Many2one(comodel_name="test.unit", string="Unit", required=False, )

class TESTUNITTYPE(models.Model):
    _name = 'test.unit'
    _rec_name = 'name'
    _description = 'Test Unit'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=False, )
