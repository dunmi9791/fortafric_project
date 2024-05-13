# -*- coding: utf-8 -*-
# from odoo import http


# class FortafricProjects(http.Controller):
#     @http.route('/fortafric_projects/fortafric_projects', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fortafric_projects/fortafric_projects/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fortafric_projects.listing', {
#             'root': '/fortafric_projects/fortafric_projects',
#             'objects': http.request.env['fortafric_projects.fortafric_projects'].search([]),
#         })

#     @http.route('/fortafric_projects/fortafric_projects/objects/<model("fortafric_projects.fortafric_projects"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fortafric_projects.object', {
#             'object': obj
#         })

