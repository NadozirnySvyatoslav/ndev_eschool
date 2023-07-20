{
    'name': "eSchool",
    'version': '16.0.1.0.0',
    'category': 'Human Resources/School',

    'summary': """
        School management
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
        'views/class_views.xml',
        'views/year_views.xml',
        'views/eschool_menus.xml',

        'wizard/open_journal_view.xml',

    ],
    'demo': [
        'demo/subjects_data.xml',
        'demo/year_data.xml',
        'demo/class_data.xml',
        # 'demo/pupil_data.xml',
        # 'demo/parent_data.xml',
        # 'demo/teacher_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ndev_eschool/static/src/js/kanban_one2many_names.js',
            'ndev_eschool/static/src/xml/kanban_one2many_names.xml',
            'ndev_eschool/static/src/xml/timetable_lines.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
    'price': 9.99,
    'currency': 'EUR'
}
