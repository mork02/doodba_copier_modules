{
    'name': 'Save name',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Simply enter ur name and save it.',
    'description': """Saves your name on odoo.""",
    'author': 'KeDeX',
    'website': 'https://github.com/mork02/doodba_copier_modules/tree/main/KDX_save_name',
    'depends': ['base'],
    'data': [
        'views/save_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}