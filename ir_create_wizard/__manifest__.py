{
    'name': 'Create Wizard',
    "version": "11.0.1.0.0",
    "author": "SIRUM GmbH",
    "website": "https://www.sirum.de/",
    "category": "custom",
    "license": "SEL-1",
    'depends': ['base', 'web'],
    'data': [
        'views/ir_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/js/ir_wizard.js',
        ],
    },
    'installable': True,
    'application': False,
}
