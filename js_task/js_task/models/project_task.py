from odoo import fields, models,api


class Product(models.Model):
    _inherit = "project.task"


    @api.onchange('stage_id')
    def _onchange_state(self):
    	if self.stage_id.id==3:
    		a=self.env['my.demo'].create({
    			'task_id':self.id,
    			})
    		print("----------------",a)	

