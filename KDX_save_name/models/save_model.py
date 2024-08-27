from odoo import models, fields

class SaveName(models.Model):
    _name = "save.name"
    _description = "Add a name and save it"

    first_name = fields.Char(string="Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
