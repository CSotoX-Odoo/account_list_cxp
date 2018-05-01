# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 28/ABR/2018 (CSOTOX)

{
    'name': 'Account_Listado_CxP',
    'version': '11.1.0 - Beta',
    'category': 'Account',
    'sequence': 10,
    'author' : 'Carlos Rafael Soto (CSOTOX)',
    'summary': 'AddOn de mejoras a CXP',
    'description': """
                    Versión de Odoo: 11
                    """,
    'website': 'https://github.com/OdooX/account_list_cxp',
    'depends': [
        'account',
        ],
    'data': [
        'views/listado_cxp.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}