# File: tests/test_ir_attachments_zip_download.py

import odoo.tests.common as common
from odoo.exceptions import UserError


class TestIrAttachmentDownload(common.TransactionCase):
    def setUp(self):
        super(TestIrAttachmentDownload, self).setUp()
        # Create test data: binary attachment and non-binary attachment
        self.attachment_model = self.env["ir.attachment"]

        # Create a binary attachment
        self.attachment_binary = self.attachment_model.create(
            {
                "name": "test_binary.txt",
                "datas": "Test data",
                "type": "binary",
                "res_model": "res.partner",
                "res_id": self.env.ref("base.res_partner_1").id,
            }
        )

        # Create a non-binary attachment
        self.attachment_non_binary = self.attachment_model.create(
            {
                "name": "test_url.txt",
                "url": "http://example.com",
                "type": "url",
                "res_model": "res.partner",
                "res_id": self.env.ref("base.res_partner_1").id,
            }
        )

    def test_download_binary_attachment(self):
        # Test if the download works for binary attachments
        action = self.attachment_binary.action_attachments_download()
        self.assertEqual(
            action["type"], "ir.actions.act_url", "The action type should be a URL."
        )
        self.assertIn(
            "/web/attachment/download_zip",
            action["url"],
            "The URL should point to the zip download.",
        )

    def test_non_binary_attachments_error(self):
        # Test that a UserError is raised when a non-binary attachment is selected
        with self.assertRaises(UserError):
            self.attachment_non_binary.action_attachments_download()

    def test_no_attachment_selected_error(self):
        # Test that a UserError is raised when no attachment is selected
        empty_recordset = self.attachment_model.browse()
        with self.assertRaises(UserError):
            empty_recordset.action_attachments_download()

    def test_zip_file_creation(self):
        # Test the zip file creation process
        zip_file = self.attachment_binary._create_temp_zip()
        self.assertIsNotNone(zip_file, "The zip file should be created successfully.")
        self.assertTrue(zip_file.readable(), "The zip file should be readable.")
