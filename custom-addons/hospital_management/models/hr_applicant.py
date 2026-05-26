from odoo import models, fields


class HrApplicantExtended(models.Model):
    _inherit = 'hr.applicant'

    medical_license_number = fields.Char(
        string='Medical License No.',
        help='Official medical license number for compliance tracking'
    )

    license_expiry_date = fields.Date(
        string='License Expiry Date',
        help='Date when the medical license expires'
    )