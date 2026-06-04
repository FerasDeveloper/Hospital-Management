from odoo import models, fields, api


class HospitalDashboard(models.Model):
    _name = "hospital.dashboard"
    _description = "Hospital Dashboard"

    total_patients = fields.Integer(readonly=True)
    total_doctors = fields.Integer(readonly=True)
    total_appointments = fields.Integer(readonly=True)
    done_appointments = fields.Integer(readonly=True)
    cancelled_appointments = fields.Integer(readonly=True)

    patient_ids = fields.One2many('hospital.patient', compute='_compute_patient_ids')
    doctor_ids = fields.One2many('hospital.doctor', compute='_compute_doctor_ids')
    appointment_ids = fields.One2many('hospital.appointment', compute='_compute_appointment_ids')

    @api.depends()
    def _compute_patient_ids(self):
        for record in self:
            record.patient_ids = self.env['hospital.patient'].search([])

    @api.depends()
    def _compute_doctor_ids(self):
        for record in self:
            record.doctor_ids = self.env['hospital.doctor'].search([])
    patient_ids = fields.Many2many(
        "hospital.patient",
        readonly=True
    )

    doctor_ids = fields.Many2many(
        "hospital.doctor",
        readonly=True
    )

    appointment_ids = fields.Many2many(
        "hospital.appointment",
        readonly=True
    )

    @api.model
    def get_dashboard_data(self):

        dashboard = self.create({
            "total_patients":
                self.env["hospital.patient"].search_count([]),

            "total_doctors":
                self.env["hospital.doctor"].search_count([]),

            "total_appointments":
                self.env["hospital.appointment"].search_count([]),

            "done_appointments":
                self.env["hospital.appointment"].search_count([
                    ("status", "=", "done")
                ]),

            "cancelled_appointments":
                self.env["hospital.appointment"].search_count([
                    ("status", "=", "cancel")
                ]),

            "patient_ids": [(
                6,
                0,
                self.env["hospital.patient"].search([]).ids
            )],

            "doctor_ids": [(
                6,
                0,
                self.env["hospital.doctor"].search([]).ids
            )],

            "appointment_ids": [(
                6,
                0,
                self.env["hospital.appointment"].search([], limit=10).ids
            )],
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Dashboard",
            "res_model": "hospital.dashboard",
            "view_mode": "form",
            "res_id": dashboard.id,
            "target": "current",
        }

    def action_print_report(self):

        return self.env.ref(
            "hospital_management.action_dashboard_report"
        ).report_action(self)