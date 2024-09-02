{
    'name': 'tms_attachment_navigation',
    'version': '1.0',
    'summary': 'Adds a button to TMS form to navigate to ir.attachment tree view.',
    'description': """
        This module adds a button on the TMS order form view to navigate directly to the ir.attachment tree view.
    """,
    'author': 'KeDeX',
    'website': 'none',
    'category': 'Transport Management',
    'depends': ['base', 'tms_base'],
    'data': [
        'views/navigate_attachment.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}