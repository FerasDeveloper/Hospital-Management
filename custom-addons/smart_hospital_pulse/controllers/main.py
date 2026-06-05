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

            if not ticket_id or heart_rate is None:
                return {
                    'status': 'error',
                    'message': 'ticket_id and heart_rate are required'
                }

            ticket = request.env['crm.lead'].sudo().search(
                [('id', '=', ticket_id)],
                limit=1
            )

            if not ticket:
                return {
                    'status': 'error',
                    'message': f'Ticket {ticket_id} not found'
                }

            ticket.write({
                'patient_heart_rate': heart_rate
            })

            return {
                'status': 'ok',
                'ticket_id': ticket_id,
                'heart_rate': heart_rate,
                'is_critical': ticket.is_critical_iot_alert
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }