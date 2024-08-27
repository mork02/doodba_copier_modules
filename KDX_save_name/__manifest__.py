{
    'name': 'Save name',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Simply enter your name and save it.',
    'description': """Saves your name on Odoo.""",
    'author': 'KeDeX',
    'website': 'https://github.com/mork02/doodba_copier_modules/tree/main/KDX_save_name',
    'depends': ['base'],
    'data': [
        'views/save_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
