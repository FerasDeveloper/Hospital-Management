from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"

    name = fields.Char(string="Doctor Name", required=True)

    age = fields.Integer(string="Age")

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")

    phone = fields.Char(string="Phone")

    email = fields.Char(string="Email")

    specialization = fields.Char(string="Specialization")

    salary = fields.Float(string="Salary")

    employee_id = fields.Many2one("hr.employee", string="Related Employee")

    user_id = fields.Many2one("res.users", string="Related User")

    active = fields.Boolean(default=True)

    appointment_ids = fields.One2many(
        "hospital.appointment", "doctor_id", string="Appointments"
    )

    appointment_count = fields.Integer(
        string="Appointments Count", compute="_compute_appointment_count"
    )

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = len(rec.appointment_ids)

    def action_view_appointments(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Appointments",
            "view_mode": "list,form",
            "res_model": "hospital.appointment",
            "domain": [("doctor_id", "=", self.id)],
        }
