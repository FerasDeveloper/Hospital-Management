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
        # استقبال البيانات القادمة من الـ params في Postman تلقائياً
        ticket_id = kwargs.get('ticket_id')
        heart_rate = kwargs.get('heart_rate')

        if not ticket_id or heart_rate is None:
            return {
                'status': 'error',
                'message': 'Missing fields: ticket_id or heart_rate'
            }

        # البحث عن التيكيت وتحديثها
        lead = request.env['crm.lead'].sudo().browse(int(ticket_id))
        if not lead.exists():
            return {
                'status': 'error',
                'message': f'Ticket ID {ticket_id} not found'
            }

        # تحديث قيمة النبض (سيقوم بتشغيل دالة write والبزنس لوجيك تلقائياً)
        lead.sudo().write({'patient_heart_rate': int(heart_rate)})

        return {
            'status': 'success',
            'message': 'Vitals updated successfully',
            'is_critical': lead.is_critical_iot_alert
        }