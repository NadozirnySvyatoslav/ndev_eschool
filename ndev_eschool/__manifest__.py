{
    'name': "E-School",
    'version': '16.0.1.0.0',
    'category': 'Human Resources/School',

    'summary': """
        E-School school electronic document management
        """,

    'author': "Svyatoslav Nadozirny",
    'website': "https://ndev.online",
    'maintainer': 'NDev',
    'depends': ['hr', 'portal', 'mail'],
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',

        'views/journal_views.xml',
        'views/teacher_views.xml',
        'views/pupil_views.xml',
        'views/parent_views.xml',
        'views/schedule_views.xml',
        'views/subject_views.xml',
        'views/lesson_views.xml',
        'views/class_views.xml',
        'views/eschool_menus.xml',

    ],
    'demo': [
        'demo/subjects_data.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3'
}
