from odoo.http import request
from odoo import http

class OrdeNote(http.Controller):


    @http.route('/mypage',type='http', auth="public", website=True) 
    def open_page(self,**kw):
        return request.render("js_task.my_page",{}) 