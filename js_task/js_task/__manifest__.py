# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Js Task",
    "version": "16.0.1.0.0",
    "summary": "Js Task",
    "sequence": 10,
    "description": """
Product Order Note""",
    "depends": ["website_sale"],
    "data": [
    "security/ir.model.access.csv",
    'views/my_page.xml',
    # 'views/template.xml',
    # 'views/product.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'js_task/static/src/js/my_js.js',
        ],
    },
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
