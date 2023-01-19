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
    'demo':[
        'demo/tour_demo.xml',
        'demo/destination_demo.xml',
        'demo/tour_package_demo.xml',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'views/tour_menu.xml',
        'views/tour_package.xml',      
        'views/tour_admin.xml',        
         'views/tour_booking.xml',  
        
     ],
'auto_install': False  

}