# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#in order to setup multi companies to be used for this inventory system, go to settings and select the company link to create companies,after which users 
#can be created under settings as well and linked to the any of the created companies. The created companies appear as options on the inventory register form and 
#can be linked to specifc drugs registered.Also ensure that manage multiple companies under general settings is checked

{
    'name': 'Ludendorf Inventory management',
    'version': '1.0.1',
    'description': 'drug inventory ',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'data': ['views/lf_register_view.xml',
             'views/lf_request_view.xml',
             'menu/lf_inventory_menu.xml',
             'data/ir_sequence_data.xml'
            ],
    
}
