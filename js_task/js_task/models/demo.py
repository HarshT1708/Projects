from odoo import fields, models,api

class custom(models.Model):
	_name='my.demo'

	task_id=fields.Many2one('project.task')
	name=fields.Char(related="task_id.name",store=True)
	stage_id_realted=fields.Many2one(related="task_id.stage_id")

	@api.onchange('stage_id_realted')
	def _onchange_stage(self):
		print("--------------------",self.stage_id_realted)

