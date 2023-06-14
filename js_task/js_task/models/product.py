# from googletrans import Translator
# from odoo import fields, models,api


# class Product(models.Model):
#     _inherit = "product.template"

#     translated_product = fields.Char(string="Translated",compute="_compute_product_name")


#     @api.depends('name')
#     def _compute_product_name(self):
#         source_language = 'en'
#         destination_language = 'ar'
#         main_product_name = self.name
#         translator = Translator()
#         result = translator.translate(main_product_name, src=source_language, dest=destination_language)
#         if main_product_name:
#             self.translated_product = result.text
#         else:
#             self.translated_product=""
                

