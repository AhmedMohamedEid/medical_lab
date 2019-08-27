from odoo import api, fields, models


class LABREQUEST(models.Model):
    _name = 'lab.request'
    _rec_name = 'code'
    _description = 'Lab Request'

    code = fields.Char(string="Code", required=False, )
    patient_result_id = fields.Many2one(comodel_name="mdc.lab.patient", string="Patient", required=True, )
    lab_test_id = fields.Many2one(comodel_name='lab.test', string="Lab Test")
    request_date = fields.Datetime(string="Request Date", default=fields.Datetime.now, required=False, )
    # lab_content_ids = fields.Many2many(comodel_name="lab.test.type",  string="sub test", )
    content_ids = fields.One2many(comodel_name="test.content.result", inverse_name="request_id", string="Content", required=False, )

    @api.model
    def create(self, values):
        values.update({'code': self.env['ir.sequence'].next_by_code('leb.request')})
        session_self__create = super(LABREQUEST, self).create(values)
        print(values)
        print(session_self__create.id)
        test_content = self.env['test.content.result']
        for content in  self.env["lab.test.type"].search([("lab_test_id.id","=", values["lab_test_id"])]):
            print(content)
            test_content.create({
                "request_id" : session_self__create.id,
                "content_type_id" :content.id ,
                "result" : 0,
            })

        return session_self__create

    # @api.multi
    # def write(self, values):
    #     test_content = self.env['test.content.result']
    #     for content in self.env["lab.test.type"].search([("lab_test_id.id", "=", self.lab_test_id.id)]):
    #         print(content)
    #         test_content.create({
    #             "request_id": self.id,
    #             "content_type_id": content.id,
    #             "result": 0,
    #         })
    #     return super(LABREQUEST, self).write(values)

class LABTESTCONTENT(models.Model):
    _name = 'test.content.result'
    _description = 'Lab Test Content Result'

    request_id = fields.Many2one(comodel_name="lab.request", string="Request", required=True, )
    test_id = fields.Many2one(related="request_id.lab_test_id")
    content_type_id = fields.Many2one(comodel_name="lab.test.type", string="Content", required=True, )

    result = fields.Float(string="Result", required=False, )