# -*- coding: utf-8 -*-
{
    'name': "ekinerja",

    'summary': """
        e-kinerja merupakan aplikasi berbasis web untuk melakukan pendataan terkait kinerja mahasiswa""",

    'description': """
        e-kinerja merupakan aplikasi menggunakan platform odoo-15
    """,

    'author': "Midori No Ken",
    'website': "http://www.bit.ly/MidoriNoKen",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
