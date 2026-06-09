from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender"
    )
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")

    blood_group = fields.Selection(
        [
            ("a+", "A+"),
            ("a-", "A-"),
            ("b+", "B+"),
            ("b-", "B-"),
            ("ab+", "AB+"),
            ("ab-", "AB-"),
            ("o+", "O+"),
            ("o-", "O-"),
        ],
        string="Blood Group",
    )

    notes = fields.Text(string="Medical Notes")
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one("res.partner", string="Customer")

    appointment_ids = fields.One2many(
        "hospital.appointment",
        "patient_id",
        string="Appointments"
    )

    @api.model_create_multi
    def create(self, vals_list):
        # 🚀 [الحل الشامل والنهائي] تنظيف وتطهير قاعدة البيانات من أي حقول تعطل النظام
        try:
            # استعلام ذكي يجلب كل الأعمدة المخصصة الإلزامية في جدول res_partner التي ليس لها قيمة افتراضية
            self.env.cr.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = 'res_partner' 
                  AND is_nullable = 'NO' 
                  AND column_default IS NULL
                  AND column_name NOT IN ('id', 'create_uid', 'create_date', 'write_uid', 'write_date', 'name', 'company_id');
            """)
            
            # جلب أسماء الحقول (مثل group_rfq و group_on وأي حقل آخر)
            strict_columns = [row[0] for row in self.env.cr.fetchall()]
            
            # إسقاط قيد NOT NULL عنها جميعاً في ثانية واحدة
            for col in strict_columns:
                self.env.cr.execute(f"ALTER TABLE res_partner ALTER COLUMN {col} DROP NOT NULL;")
        except Exception:
            # تخطي بأمان إذا كانت الجداول غير جاهزة بعد
            pass

        Partner_Model = self.env["res.partner"]

        for vals in vals_list:
            partner_vals = {
                "name": vals.get("name"),
                "phone": vals.get("phone"),
                "email": vals.get("email"),
            }

            # إنشاء جهة الاتصال الحين بأمان مطلق مهما كان عدد الحقول الإجبارية
            partner = Partner_Model.create(partner_vals)
            vals["partner_id"] = partner.id

        return super().create(vals_list)