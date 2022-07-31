{
    'name': 'Real-State',
    'version': 'not declered',
    'category': '14',
    'lincense': 'LGPL-3',
    'summary': 'Track leads and close opportunities',
    'description': 'this is real state module',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menu.xml'
    ],
    'application': True,
    'instaliable': True,
    'auto-install': False,
}
