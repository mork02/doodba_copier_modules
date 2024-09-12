from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    exclude_js_files = fields.Boolean(string="Exclude .js files")
    exclude_css_files = fields.Boolean(string="Exclude .css files")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        # Store parameters with the correct key
        self.env["ir.config_parameter"].sudo().set_param(
            "my_module.exclude_js_files", self.exclude_js_files
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "my_module.exclude_css_files", self.exclude_css_files
        )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # Retrieve parameters with the correct key
        res.update(
            exclude_js_files=self.env["ir.config_parameter"]
            .sudo()
            .get_param("my_module.exclude_js_files", default=False),
            exclude_css_files=self.env["ir.config_parameter"]
            .sudo()
            .get_param("my_module.exclude_css_files", default=False),
        )
        return res
