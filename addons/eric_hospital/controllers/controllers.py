# -*- coding: utf-8 -*-
from odoo import http

# class EricHospital(http.Controller):
#     @http.route('/eric_hospital/eric_hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eric_hospital/eric_hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eric_hospital.listing', {
#             'root': '/eric_hospital/eric_hospital',
#             'objects': http.request.env['eric_hospital.eric_hospital'].search([]),
#         })

#     @http.route('/eric_hospital/eric_hospital/objects/<model("eric_hospital.eric_hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eric_hospital.object', {
#             'object': obj
#         })