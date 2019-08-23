from odoo import api, fields, models

class LABCONTENT(models.Model):
    _name = 'lab.test.type'
    _rec_name = 'name'
    _description = 'Lab Test Type'

    name = fields.Char(string="Name", required=True, )
    lab_test_id = fields.Many2one(comodel_name="lab.test", string="Lab Test", required=True, )
    result = fields.Char(string="result", required=False, )
