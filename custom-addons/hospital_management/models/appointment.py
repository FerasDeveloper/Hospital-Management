from odoo import models, fields


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(
        "hospital.patient",
        string="Patient",
        required=True
    )

    doctor_id = fields.Many2one(
        "hospital.doctor",
        string="Doctor",
        required=True
    )

    appointment_date = fields.Datetime(
        string="Appointment Date",
        required=True
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        default="draft",
    )

    notes = fields.Text(string="Notes")

    def action_confirm(self):
        self.status = "confirmed"

    def action_done(self):
        self.status = "done"

    def action_cancel(self):
        self.status = "cancel"

    def action_draft(self):
        self.status = "draft"