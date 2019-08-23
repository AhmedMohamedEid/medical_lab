# -*- coding: utf-8 -*-
from odoo import http

# class MdcLab(http.Controller):
#     @http.route('/mdc_lab/mdc_lab/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mdc_lab/mdc_lab/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mdc_lab.listing', {
#             'root': '/mdc_lab/mdc_lab',
#             'objects': http.request.env['mdc_lab.mdc_lab'].search([]),
#         })

#     @http.route('/mdc_lab/mdc_lab/objects/<model("mdc_lab.mdc_lab"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mdc_lab.object', {
#             'object': obj
#         })