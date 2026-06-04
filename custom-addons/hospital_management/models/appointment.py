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

    amount = fields.Float(
        string="Amount",
        default=100
    )

    invoice_id = fields.Many2one(
        "account.move",
        string="Invoice"
    )

    payment_state = fields.Selection(
        related="invoice_id.payment_state",
        string="Payment Status",
        readonly=True
    )

    def action_confirm(self):
        self.status = "confirmed"

    def action_done(self):

        self.status = "done"

        if not self.invoice_id:

            invoice = self.env["account.move"].create({
                "move_type": "out_invoice",

                "partner_id": self.patient_id.partner_id.id,

                "invoice_line_ids": [(0, 0, {
                    "name": "Medical Appointment",
                    "quantity": 1,
                    "price_unit": self.amount,
                })]
            })

            self.invoice_id = invoice.id

    def action_cancel(self):
        self.status = "cancel"

    def action_draft(self):
        self.status = "draft"