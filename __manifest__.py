# -*- coding: utf-8 -*-
{
    'name': "Product Owner",
    'version': '17.0.1.0.0',
    'depends': ['point_of_sale'],
    'category': '',
    'description': """
    summary of this app
    """,
    'data': [
        'views/product_form_views.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            'product_owner/static/src/xml/product_owner.xml',
            'product_owner/static/src/js/product_owner.js',

        ],
    },
    'application': 'True',
    'installable': True,
}