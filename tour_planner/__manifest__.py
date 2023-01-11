{
    'name': 'Tour Planner',
    'version': '2.0',
    'description': 'Tour Planner Module',
    'author': 'odoo',
    'category': 'marketing',
    'installable': True, 
    'summary': 'Tour management Agency', 
    'application': True,
    
    'depends': [
    ],
    'data': [
        'views/tour_admin.xml',
        'security/ir.model.access.csv',
     ],
'auto_install': False    
}