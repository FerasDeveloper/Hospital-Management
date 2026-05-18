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

    active = fields.Boolean(default=True)

    appointment_ids = fields.One2many(
        "hospital.appointment", "doctor_id", string="Appointments"
    )
