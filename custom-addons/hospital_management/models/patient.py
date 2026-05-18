from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)

    age = fields.Integer(string='Age')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')

    phone = fields.Char(string='Phone')

    email = fields.Char(string='Email')

    address = fields.Text(string='Address')

    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string='Blood Group')

    notes = fields.Text(string='Medical Notes')

    active = fields.Boolean(default=True)

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string='Appointments'
    )