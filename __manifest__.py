{
    'name': 'ip_visitor_tracking',
    'version': '1.0',
    'summary': 'Integración con la API de IPGeolocation',
    'description': 'Obtención de datos gelógicos en tiempo real.',
    'author': 'Adrián Uceta Gamaza',
    'category': 'Website',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/ipgeo_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': 'ip_visitor_tracking/static/description/icon58.png',
}