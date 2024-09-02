import zipfile
from io import BytesIO

from odoo import _, models
from odoo.exceptions import UserError

class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    def action_attachments_download(self):
        items = self.filtered(lambda x: x.type == "binary")
        if not items:
            raise UserError(
                _("None attachment selected. Only binary attachments allowed.")
            )
        ids = ",".join(map(str, items.ids))
        return {
            "type": "ir.actions.act_url",
            "url": "/web/attachment/download_zip?ids=%s" % (ids),
            "target": "self",
        }

    def _create_temp_zip(self):
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for attachment in self:
                attachment.check("read")
                zip_file.writestr(
                    attachment._compute_zip_file_name(),
                    attachment.datas,  # Use 'datas' field for binary content
                )
            zip_buffer.seek(0)
        return zip_buffer

    def _compute_zip_file_name(self):
        """Give a chance of easily changing the name of the file inside the ZIP."""
        self.ensure_one()
        return self.name
