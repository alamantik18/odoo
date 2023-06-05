# -*- encoding: utf-8 -*-

{
    'name': 'Company Management',
    'category': 'Company',
    'sequence': -100,
    'summary': 'Company management system',
    'description': """Company management system""",
    'website': 'https://www.odoo.com/app/website',
    'version': '1.0.0',
    'depends': [
        'website',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/base_template.xml',
        'views/template.xml',
        'views/person_create.xml',
    ],
    'demo': [],
    'assets': {},
    'license': 'LGPL-3',
}
