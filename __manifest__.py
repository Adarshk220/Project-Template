{
    'name': 'Project Template',
    'author': 'Adarsh',
    'version': '17.0.1.0.0',
    'summary': 'This app allows your project team to create project template and task template',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_template_views.xml',
        'views/task_template_views.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
    ],
    'sequence': -100,
    'application': True,
}