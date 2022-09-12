{
    'name': 'studentapp',
    'version': '1.0.0',
    'category': 'Student Management App',
    'author': 'manthan',
    'summary': 'Student Management System',
    'description': """""",
    'depends': ['mail','base'],
    'data': [
        'security/ir.model.access.csv',
        'data/course_data.xml',
        'data/Degree_data.xml',
        'data/university_data.xml',
        'views/menu.xml' ,
        'views/studentdetails.xml',
        'views/courses_view.xml',
        'views/configuration_degree_view.xml', 
        'views/configuration_duration_view.xml',
        'views/configuration_university_view.xml' 
        
    ],
    'demo': [],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
}
