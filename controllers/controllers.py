# -*- coding: utf-8 -*-
# from odoo import http


# class Ekinerja(http.Controller):
#     @http.route('/ekinerja/ekinerja', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ekinerja/ekinerja/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ekinerja.listing', {
#             'root': '/ekinerja/ekinerja',
#             'objects': http.request.env['ekinerja.ekinerja'].search([]),
#         })

#     @http.route('/ekinerja/ekinerja/objects/<model("ekinerja.ekinerja"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ekinerja.object', {
#             'object': obj
#         })
