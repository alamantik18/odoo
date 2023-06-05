from odoo import http
from odoo.http import request


class PersonsController(http.Controller):
    @http.route('/persons', auth='public', website=True, type='http')
    def view_persons(self, **kwargs):
        records = request.env['company.persons'].search([], limit=5, order='id')
        return request.render('om_company.persons_page', {'records': records})

    @http.route(['/persons/create'], auth='public', website=True, type='http')
    def view_create_person(self, **kwargs):
        return request.render('om_company.create_person', {})

