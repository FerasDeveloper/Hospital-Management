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

        try:
            data = request.get_json_data()

            ticket_id = data.get('ticket_id')
            heart_rate = data.get('heart_rate')

            ticket = request.env['crm.lead'].sudo().search(
                [('id', '=', ticket_id)],
                limit=1
            )

            if not ticket:
                return {
                    'status': 'error',
                    'message': f'Ticket {ticket_id} not found'
                }

            return {
                'status': 'ok',
                'ticket_name': ticket.name,
                'ticket_id': ticket.id,
                'heart_rate': heart_rate
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }