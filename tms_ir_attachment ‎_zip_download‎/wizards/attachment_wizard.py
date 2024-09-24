from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AttachmentWizard(models.TransientModel):
    _name = "attachment.wizard"
    _description = "Sort Attachments by Selected Date"

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)

    @api.constrains("date_from", "date_to")
    def _check_dates(self):
        for record in self:
            if record.date_from > record.date_to:
                raise ValidationError(
                    _("The start date must be earlier than the end date.")
                )

    def apply_filter(self):
        """
        Apply the date filter and
        return the attachments filtered by the selected date range.
        """
        # Ensure date_from is earlier than date_to
        if self.date_from > self.date_to:
            raise ValidationError(
                _("The start date must be earlier than the end date.")
            )

        # Return action to open the filtered attachments in the tree and form views
        return {
            "type": "ir.actions.act_window",
            "name": _("Filtered Attachments"),
            "res_model": "ir.attachment",
            "view_mode": "tree,form",
            "domain": [
                ("create_date", ">=", self.date_from),
                ("create_date", "<=", self.date_to),
            ],
            "context": dict(self.env.context),
        }
