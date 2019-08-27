from odoo import api, fields, models


class LabTestCategory(models.Model):
    _name = 'lab_category'
    _description = 'Lab Categories'

    name = fields.Char(string="Category Name", required=False, )


class LABTEST(models.Model):
    _name = 'lab.test'
    _rec_name = 'name'
    _description = 'Lab Test and Test type'

    name = fields.Char(string="Name", required=True, )
    prefix_code = fields.Char(string="Code", required=True, )
    price = fields.Float(string="Price", required=True, )

    test_content_ids = fields.One2many(comodel_name="lab.test.type", inverse_name="lab_test_id", string="Test Contetn", required=False, )
    test_category_ids = fields.Many2one(comodel_name="lab_category", string="Category Name", required=False, )


class LABCONTENT(models.Model):
    _name = 'lab.test.type'
    _rec_name = 'name'
    _description = 'Lab Test Type'

    name = fields.Char(string="Name", required=True, )
    lab_test_id = fields.Many2one(comodel_name="lab.test", string="Lab Test", required=True, )
    start_range = fields.Float(string="Start Range",  required=False, )
    end_range = fields.Float(string="End Range",  required=False, )
    test_unit_id = fields.Many2one(comodel_name="test.unit", string="Unit", required=False, )



class TESTUNITTYPE(models.Model):
    _name = 'test.unit'
    _rec_name = 'name'
    _description = 'Test Unit'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=False, )
