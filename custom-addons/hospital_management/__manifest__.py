{
    "name": "Hospital Management",
    "version": "1.0",
    "summary": "Hospital Management System",
    "author": "Your Name",
    "category": "Management",
    # "depends": ["base"],
    "depends": ["base", "hr", "project"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/appointment_views.xml",
    ],
    "installable": True,
    "application": True,
}
