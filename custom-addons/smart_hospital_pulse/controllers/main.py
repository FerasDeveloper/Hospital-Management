from odoo import http
from odoo.http import request


class HospitalVitalsController(http.Controller):

    @http.route(
        '/api/hospital/vitals/update',
        type='json',
        auth='public',
        methods=['POST'],
        csrf=False
    )
    def update_vitals(self, **kwargs):

        return {
            'status': 'ok',
            'message': 'Controller Works'
        }